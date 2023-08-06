from __future__ import annotations

import json
import logging
import shutil
import subprocess
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from module_qc_nonelec_gui.dbinterface.lib import localdb_uploader
from module_qc_nonelec_gui.qc_tests.vi.functions.auto_trim import detect_circle
from module_qc_nonelec_gui.qc_tests.vi.functions.cv2_func import (
    cv2,
    img_rotate,
    read_img,
    write_img,
)
from module_qc_nonelec_gui.qc_tests.vi.lib import (
    auto_trimimg_win,
    inspection_win,
    loadimg_win,
    splitimg_win,
    summary_win,
    trimimg_win,
    vi_initial_win,
)

log = logging.getLogger(__name__)


class TestWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.parent = parent

        self.setGeometry(0, 0, 500, 300)

        temp_dir_path = "temp"
        try:
            Path(temp_dir_path).mkdir(parents=True)
        except FileExistsError:
            shutil.rmtree(temp_dir_path)
            Path(temp_dir_path).mkdir(parents=True)

        # window title
        self.setWindowTitle("Visual Inspection GUI")

        # list and dict of anomalies
        self.anomaly_dic = {}
        self.comment_dic = {}
        self.img_dic = {}

        # component and user information
        self.atlsn = self.parent.info_dict["component"]
        self.type_name = self.parent.info_dict["componentType"]
        # self.original_institution = self.parent.info_dict["institution"]
        # self.current_location = self.parent.info_dict["currentLocation"]
        if self.type_name == "MODULE":
            self.stage = self.parent.info_dict["currentStage"]
            self.inspector = self.parent.db_user
        else:
            self.stage = ""
            self.inspector = ""

        # load configuration file
        log.info(f"type_name = {self.type_name}")
        log.info(f"stage = {self.stage}")

        stage_alt = self.stage.replace("/", "__")

        if self.type_name == "MODULE":
            self.json_config = str(
                Path(__file__).parent
                / f"config/config_{self.type_name}_{stage_alt}.json"
            )
            self.json_reference = str(
                Path(__file__).parent
                / f"config/reference_{self.type_name}_{stage_alt}.json"
            )
        with Path(self.json_config).open() as f:
            self.config = json.load(f)
        with Path(self.json_reference).open() as f:
            self.reference = json.load(f)

        # path to golden modules
        # self.path_gm = 'qc_tests/vi/golden_module'
        self.path_gm = str(Path(__file__).parent / self.config["goldenmodule_path"])

        # check the presence of golden modules
        try:
            with Path(self.path_gm + "/main_img.jpg").open() as f:
                pass
        except Exception as e:
            log.exception("missing the golden image file: " + str(e))

            QMessageBox.warning(
                None,
                "Warning",
                "Golden module image bank is being downloaded...\nWait for a minute.",
            )

            log.info(f"Golden module not found on {self.path_gm}, deploying it...")
            subprocess.run(
                "cd /tmp; rm -rf golden_module*; curl -O https://cernbox.cern.ch/remote.php/dav/public-files/FmenidYbrKAJAdW/golden_module_20230320.zip",
                shell=True,
            )
            subprocess.run("cd /tmp; unzip golden_module_20230320.zip", shell=True)
            subprocess.run(
                "mv -f /tmp/golden_module {}".format(
                    str(Path(self.path_gm).parent.parent)
                ),
                shell=True,
            )
            subprocess.run("rm -rf /tmp/golden_module*", shell=True)

            with Path(self.path_gm + "/main_img.jpg").open() as f:
                pass

        # checked page list
        self.rev = 0
        self.tot_page = int(self.config["ntile"])
        self.nsplit = int(self.config["nsplit"])
        self.page_checked = []
        for i in range(self.tot_page):
            self.page_checked.insert(i, False)

        # check list
        self.checklist_dict = {}

        for tile in range(36):
            default = self.config["checklist"].get("default")

            if default:
                self.checklist_dict[str(tile)] = default

            if str(tile) in self.config["checklist"]:
                self.checklist_dict[str(tile)].update(
                    self.config["checklist"].get(str(tile))
                )

    def update_widget(self, w):
        self.setCentralWidget(w)
        self.show()

    def init_ui(self):
        self.initial_wid = vi_initial_win.InitialWindow(self)
        self.update_widget(self.initial_wid)

    def close_and_return(self):
        self.close()
        self.parent.back_from_test()

    def update_img(self, img):
        path = f"temp/img_{self.rev}.jpg"
        write_img(img, path)
        self.img_bgr, self.img_h, self.img_w, self.img_d = read_img(path)
        self.rev = self.rev + 1

    def undo_img(self):
        if self.rev == 0:
            self.rev = self.rev
        else:
            self.rev = self.rev - 1
        path = f"temp/img_{self.rev}.jpg"
        self.img_bgr, self.img_h, self.img_w, self.img_d = read_img(path)

    def load_img(self):
        try:
            self.img_bgr
            self.load_img_wid = loadimg_win.LoadImageWindow(self)
            self.update_widget(self.load_img_wid)
        except AttributeError:
            options = QFileDialog.Options()
            inputFileName, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                "",
                "Images (*.bmp *.dib *.pbm *.pgm *.ppm *.sr *.ras *.jpeg *.jpg *.jpe *.jp2 *.png *.tiff *.tif);;Any files (*)",
                options=options,
            )
            if not inputFileName:
                log.info("image is not chosen")
            else:
                self.statusBar().showMessage(inputFileName)
                log.info(inputFileName)

                self.img_bgr, self.img_h, self.img_w, self.img_d = read_img(
                    inputFileName
                )
                write_img(self.img_bgr, "temp/img_org.jpg")
                if self.img_h > 1000 and self.img_w > 1000:
                    self.scale = 10
                else:
                    self.scale = 1
                self.n_page = 0
                log.info("OpenCV image read success.")

                self.rev = 0

                QMessageBox.information(
                    self,
                    "Instruction",
                    'Before starting inspection, proper trimming is required.\n\n * "Rotate Image" for rotation by 90 degree for each click;\n * "Trim Image" for arranging the inspection scope;\n * Once above are done, proceed to "Split Image".',
                )

                self.load_img_wid = loadimg_win.LoadImageWindow(self)
                self.update_widget(self.load_img_wid)

    def rotate_img(self):
        # self.rotate_img_wid = rotateimg_win.RotateImageWindow(self)
        # self.update_widget(self.rotate_img_wid)
        img, h, w, d = img_rotate(self.img_bgr)
        self.update_img(img)
        self.load_img()

    def auto_trim_img(self):
        img, h, w, d = read_img("temp/img_org.jpg")
        try:
            self.circles = detect_circle(self.img_bgr)
            self.iscircle = True
            self.auto_trim_img_wid = auto_trimimg_win.TrimImageWindow(self)
            self.update_widget(self.auto_trim_img_wid)
        except Exception:
            self.img_bgr, self.img_h, self.img_w, self.img_d = read_img(
                "temp/img_org.jpg"
            )
            self.trim_img()
            self.iscircle = False

    def trim_img(self):
        self.trim_img_wid = trimimg_win.TrimImageWindow(self)
        self.update_widget(self.trim_img_wid)

    def split_img(self):
        self.split_img_wid = splitimg_win.SplitImageWindow(self)
        self.update_widget(self.split_img_wid)

    def inspection(self):
        # Guiding dialog
        self.msg_map = {
            "MODULE/ASSEMBLY": "Check carefully:\n * Glue must not reach the edge of sensor/PCB;\n * Glue does not infiltrate the pads or back-side of the sensor;\n",
            "MODULE/WIREBONDING": "Check carefully:\n * All wires match the wire bond map;\n * No shorts due to bad bonding.",
            "MODULE/PARYLENE_MASKING": "Check carefully:\n * All wires match the wire bond map;\n * No shorts due to bad bonding.",
            "MODULE/PARYLENE_COATING": "",
            "MODULE/PARYLENE_UNMASKING": "",
            "MODULE/WIREBOND_PROTECTION": "",
            "MODULE/THERMAL_CYCLES": "",
        }

        if self.n_page == 0:
            QMessageBox.information(
                self,
                "Note",
                "\n\n".join(
                    [
                        self.parent.info_dict.get("currentStage"),
                        self.msg_map.get(self.parent.info_dict.get("currentStage")),
                        "Key-binds:\n * X: Checkout Tile\n * F: Next Page\n * B: Previous Page\n * S: Switch Target/Reference",
                    ]
                ),
            )

        inspection_wid = inspection_win.InspectionWindow(self)
        self.update_widget(inspection_wid)

    def make_result(self):
        # write whole module picture
        cv2.imwrite("temp/main_img.jpg", self.img_bgr)
        path_target = "temp/main_img.jpg"
        path_reference = self.path_gm + "/main_img.jpg"

        path_target = str(
            localdb_uploader.jpeg_formatter(self.parent.localDB, path_target)
        )
        path_reference = str(
            localdb_uploader.jpeg_formatter(self.parent.localDB, path_reference)
        )
        for page, path_jpeg in self.img_dic.items():
            self.img_dic[page] = str(
                localdb_uploader.jpeg_formatter(self.parent.localDB, path_jpeg)
            )

        self.parent.testRun["results"]["Metadata"]["defects"] = self.anomaly_dic
        self.parent.testRun["results"]["Metadata"]["comments"] = self.comment_dic

        self.return_result()

    def go_to_summary(self):
        summary_wid = summary_win.SummaryWindow(self)
        self.update_widget(summary_wid)

    def return_result(self):
        self.parent.receive_result(self)
