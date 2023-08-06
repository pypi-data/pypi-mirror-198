from __future__ import annotations

import json
import logging
from pathlib import Path

from PyQt5.QtWidgets import QMainWindow

from module_qc_nonelec_gui.qc_tests.metrology.lib import initial_metrology

log = logging.getLogger(__name__)


class TestWindow(QMainWindow):
    ############################################################################################
    def __init__(self, parent=None):
        #        super(QMainWindow, self).__init__(parent)
        super(QMainWindow, self).__init__()
        self.parent = parent

        self.setGeometry(0, 0, 510, 255)

        self.result_info = {
            "distance top": "",
            "distance left": "",
            "distance right": "",
            "distance bottom": "",
            "angle top-left": "",
            "angle top-right": "",
            "angle bottom-left": "",
            "angle bottom-right": "",
            "module thickness pickup area chip1": "",
            "module thickness pickup area chip2": "",
            "module thickness pickup area chip3": "",
            "module thickness pickup area chip4": "",
            "module thickness edge chip1": "",
            "module thickness edge chip2": "",
            "module thickness edge chip3": "",
            "module thickness edge chip4": "",
            "module thickness HV capacitor": "",
            "module thickness Data connector": "",
            "planarity vacuum on": "",
            "planarity vacuum on std dev": "",
            "planarity vacuum off": "",
            "planarity vacuum off std dev": "",
            #            'program' :'',
            "program_path": "",
            "comment": "",
            "filename": "",
        }

        self.componentType = "MODULE"
        self.stage = "MODULE"

        self.init_ui()

    def receive_result(self, _result, comment):
        #        self.result_dict['filename'] = self.edit_result.text()
        with Path(self.result_info["filename"]).open() as f:
            result_dict = json.load(f)

        distance_top = result_dict["PCB to sensor edge distance top"]
        distance_left = result_dict["PCB to sensor edge distance bottom"]
        distance_right = result_dict["PCB to ASIC edge distance left"]
        distance_bottom = result_dict["PCB to ASIC edge distance right"]
        angle_top_left = result_dict[
            "Angle between PCB edge and sensor edge (top/left)"
        ]
        angle_top_right = result_dict[
            "Angle between PCB edge and sensor edge (top/right)"
        ]
        angle_bottom_left = result_dict[
            "Angle between PCB edge and sensor edge (bottom/left)"
        ]
        angle_bottom_right = result_dict[
            "Angle between PCB edge and sensor edge (bottom/right)"
        ]
        pickup_chip1 = result_dict["Thickness pickup area chip1~4"][0]
        pickup_chip2 = result_dict["Thickness pickup area chip1~4"][1]
        pickup_chip3 = result_dict["Thickness pickup area chip1~4"][2]
        pickup_chip4 = result_dict["Thickness pickup area chip1~4"][3]
        edge_chip1 = result_dict["Thickness edge chip1~4"][0]
        edge_chip2 = result_dict["Thickness edge chip1~4"][1]
        edge_chip3 = result_dict["Thickness edge chip1~4"][2]
        edge_chip4 = result_dict["Thickness edge chip1~4"][3]
        HV_capacitor = result_dict["Thickness HV capacitor"]
        Data_connector = result_dict["Thickness data connector"]
        planarity = result_dict["Planarity vacuum on/off"]
        planarity_std = result_dict["Planarity vacuum on/off std. dev."]

        self.result_info["distance top"] = distance_top
        self.result_info["distance left"] = distance_left
        self.result_info["distance right"] = distance_right
        self.result_info["distance bottom"] = distance_bottom
        self.result_info["angle top-left"] = angle_top_left
        self.result_info["angle top-right"] = angle_top_right
        self.result_info["angle bottom-left"] = angle_bottom_left
        self.result_info["angle bottom-right"] = angle_bottom_right
        self.result_info["module thickness pickup area chip1"] = pickup_chip1
        self.result_info["module thickness pickup area chip2"] = pickup_chip2
        self.result_info["module thickness pickup area chip3"] = pickup_chip3
        self.result_info["module thickness pickup area chip4"] = pickup_chip4
        self.result_info["module thickness edge chip1"] = edge_chip1
        self.result_info["module thickness edge chip2"] = edge_chip2
        self.result_info["module thickness edge chip3"] = edge_chip3
        self.result_info["module thickness edge chip4"] = edge_chip4
        self.result_info["module thickness HV capacitor"] = HV_capacitor
        self.result_info["module thickness Data connector"] = Data_connector
        self.result_info["planarity vacuum on"] = planarity
        self.result_info["planarity vacuum on std dev"] = planarity_std
        self.result_info["planarity vacuum off"] = planarity
        self.result_info["planarity vacuum off std dev"] = planarity_std

        self.result_info["comment"] = comment

        self.fill_result()

    def fill_result(self):
        self.test_result_dict = {
            "results": {
                "localDB": {
                    "distance top": self.result_info["distance top"],
                    "distance left": self.result_info["distance left"],
                    "distance right": self.result_info["distance right"],
                    "distance bottom": self.result_info["distance bottom"],
                    "angle top-left": self.result_info["angle top-left"],
                    "angle top-right": self.result_info["angle top-right"],
                    "angle bottom-left": self.result_info["angle bottom-left"],
                    "angle bottom-right": self.result_info["angle bottom-right"],
                    "module thickness pickup area chip1": self.result_info[
                        "module thickness pickup area chip1"
                    ],
                    "module thickness pickup area chip2": self.result_info[
                        "module thickness pickup area chip2"
                    ],
                    "module thickness pickup area chip3": self.result_info[
                        "module thickness pickup area chip3"
                    ],
                    "module thickness pickup area chip4": self.result_info[
                        "module thickness pickup area chip4"
                    ],
                    "module thickness edge chip1": self.result_info[
                        "module thickness edge chip1"
                    ],
                    "module thickness edge chip2": self.result_info[
                        "module thickness edge chip2"
                    ],
                    "module thickness edge chip3": self.result_info[
                        "module thickness edge chip3"
                    ],
                    "module thickness edge chip4": self.result_info[
                        "module thickness edge chip4"
                    ],
                    "module thickness HV capacitor": self.result_info[
                        "module thickness HV capacitor"
                    ],
                    "module thickness Data connector": self.result_info[
                        "module thickness Data connector"
                    ],
                    "planarity vacuum on": self.result_info["planarity vacuum on"],
                    "planarity vacuum on std dev": self.result_info[
                        "planarity vacuum on std dev"
                    ],
                    "planarity vacuum off": self.result_info["planarity vacuum off"],
                    "planarity vacuum off std dev": self.result_info[
                        "planarity vacuum off std dev"
                    ],
                    "comment": self.result_info["comment"],
                },
                "ITkPD": {
                    "distance top": self.result_info["distance top"],
                    "distance left": self.result_info["distance left"],
                    "distance right": self.result_info["distance right"],
                    "distance bottom": self.result_info["distance bottom"],
                    "angle top-left": self.result_info["angle top-left"],
                    "angle top-right": self.result_info["angle top-right"],
                    "angle bottom-left": self.result_info["angle bottom-left"],
                    "angle bottom-right": self.result_info["angle bottom-right"],
                    "module thickness pickup area chip1": self.result_info[
                        "module thickness pickup area chip1"
                    ],
                    "module thickness pickup area chip2": self.result_info[
                        "module thickness pickup area chip2"
                    ],
                    "module thickness pickup area chip3": self.result_info[
                        "module thickness pickup area chip3"
                    ],
                    "module thickness pickup area chip4": self.result_info[
                        "module thickness pickup area chip4"
                    ],
                    "module thickness edge chip1": self.result_info[
                        "module thickness edge chip1"
                    ],
                    "module thickness edge chip2": self.result_info[
                        "module thickness edge chip2"
                    ],
                    "module thickness edge chip3": self.result_info[
                        "module thickness edge chip3"
                    ],
                    "module thickness edge chip4": self.result_info[
                        "module thickness edge chip4"
                    ],
                    "module thickness HV capacitor": self.result_info[
                        "module thickness HV capacitor"
                    ],
                    "module thickness Data connector": self.result_info[
                        "module thickness Data connector"
                    ],
                    "planarity vacuum on": self.result_info["planarity vacuum on"],
                    "planarity vacuum on std dev": self.result_info[
                        "planarity vacuum on std dev"
                    ],
                    "planarity vacuum off": self.result_info["planarity vacuum off"],
                    "planarity vacuum off std dev": self.result_info[
                        "planarity vacuum off std dev"
                    ],
                    "comment": self.result_info["comment"],
                },
                "summary": {
                    "distance top": self.result_info["distance top"],
                    "distance left": self.result_info["distance left"],
                    "distance right": self.result_info["distance right"],
                    "distance bottom": self.result_info["distance bottom"],
                    "angle top-left": self.result_info["angle top-left"],
                    "angle top-right": self.result_info["angle top-right"],
                    "angle bottom-left": self.result_info["angle bottom-left"],
                    "angle bottom-right": self.result_info["angle bottom-right"],
                    "module thickness pickup area chip1": self.result_info[
                        "module thickness pickup area chip1"
                    ],
                    "module thickness pickup area chip2": self.result_info[
                        "module thickness pickup area chip2"
                    ],
                    "module thickness pickup area chip3": self.result_info[
                        "module thickness pickup area chip3"
                    ],
                    "module thickness pickup area chip4": self.result_info[
                        "module thickness pickup area chip4"
                    ],
                    "module thickness edge chip1": self.result_info[
                        "module thickness edge chip1"
                    ],
                    "module thickness edge chip2": self.result_info[
                        "module thickness edge chip2"
                    ],
                    "module thickness edge chip3": self.result_info[
                        "module thickness edge chip3"
                    ],
                    "module thickness edge chip4": self.result_info[
                        "module thickness edge chip4"
                    ],
                    "module thickness HV capacitor": self.result_info[
                        "module thickness HV capacitor"
                    ],
                    "module thickness Data connector": self.result_info[
                        "module thickness Data connector"
                    ],
                    "planarity vacuum on": self.result_info["planarity vacuum on"],
                    "planarity vacuum on std dev": self.result_info[
                        "planarity vacuum on std dev"
                    ],
                    "planarity vacuum off": self.result_info["planarity vacuum off"],
                    "planarity vacuum off std dev": self.result_info[
                        "planarity vacuum off std dev"
                    ],
                    "comment": self.result_info["comment"],
                },
            }
        }

        log.info("[Test Result file] " + self.result_info["filename"])
        self.return_result()

    ############################################################################################
    def init_ui(self):
        self.initial_bare_wid = initial_metrology.InitialWindow(self)
        self.update_widget(self.initial_bare_wid)

    def update_widget(self, w):
        self.setCentralWidget(w)
        self.show()

    def close_and_return(self):
        self.close()
        self.parent.back_from_test()

    def back_page(self):
        self.parent.init_ui()

    def back_window(self):
        self.parent.receive_backpage()

    def call_another_window(self, window):
        self.hide()
        window.init_ui()

    def return_result(self):
        #        filename_result = "output_result_summary.json"
        #        if self.componentType == "MODULEBARE":

        self.parent.receive_result(self, self.test_result_dict)
