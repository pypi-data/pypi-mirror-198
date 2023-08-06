from __future__ import annotations

import logging

from PyQt5.QtWidgets import QMainWindow

from module_qc_nonelec_gui.qc_tests.pullup.lib import initial_Pullup

log = logging.getLogger(__name__)


class TestWindow(QMainWindow):
    ############################################################################################
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__()
        self.parent = parent

        self.setWindowTitle("Pullup Resistor")

        self.result_info = {
            "choices_resistor": [150, 300, None],
            "bare_name": self.parent.info_dict["bare_module"],
            "bare_code": self.parent.info_dict["bare_module_code"],
            "FE_version": self.parent.info_dict["FE_version"],
            "N_chip": self.parent.info_dict["chip_quantity"],
            "ComponentTypeCode": self.parent.info_dict["typeCode"],
            "type             ": self.parent.info_dict["type"],
            "value": {},
            "unit": "kiloohm",
            "comment": "",
        }
        for i in range(self.result_info["N_chip"]):
            self.result_info["chip" + str(i + 1)] = ""

    def receive_result(self, value_dict, comment):
        self.result_info["value"] = value_dict
        self.result_info["comment"] = comment

        self.fill_result()
        self.return_result()

    def fill_result(self):
        self.test_result_dict = {
            "results": {
                "localDB": {
                    "value": self.result_info["value"],
                    "unit": self.result_info["unit"],
                    "comment": self.result_info["comment"],
                },
                "ITkPD": {
                    "value": self.result_info["value"],
                    "unit": self.result_info["unit"],
                    "comment": self.result_info["comment"],
                },
                "summary": {
                    "value": self.result_info["value"],
                    "unit": self.result_info["unit"],
                    "comment": self.result_info["comment"],
                },
            }
        }
        log.info(
            "[Test Result] "
            + str(self.test_result_dict["results"]["localDB"]["value"])
            + " "
            + self.test_result_dict["results"]["localDB"]["unit"]
        )

    ###########################################################################################

    def init_ui(self):
        self.initial_wid = initial_Pullup.InitialWindow(self)
        self.update_widget(self.initial_wid)

    def scale_window(self, x, y):
        self.setGeometry(0, 0, x, y)

    def update_widget(self, w):
        #        self.scale_window(510,425)
        self.scale_window(640, 480)
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
        self.parent.receive_result(self, self.test_result_dict)
