from __future__ import annotations

import logging

from PyQt5.QtWidgets import QMainWindow

from module_qc_nonelec_gui.qc_tests.sldo_vi.lib import initial_SLDO_VI

log = logging.getLogger(__name__)


class TestWindow(QMainWindow):
    ##############################################################################################
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__()
        self.parent = parent

        self.setWindowTitle("SLDO")

        self.result_info = {
            "choices_startup_grade": [
                [1, "1: -35C"],
                [2, "2: -20C"],
                [3, "3: -5C"],
                [4, "4:  10C"],
                [5, "5:  30C"],
            ],
            "startup_grade": 1,
            "comment": "",
            "filename": "",
        }

    def receive_result(self, grade, result, comment):
        self.result_info["startup_grade"] = grade
        self.result_info["result"] = result
        self.result_info["comment"] = comment

        self.fill_result()
        self.return_result()

    def fill_result(self):
        self.test_result_dict = {
            "results": {
                "localDB": self.result_info["result"],
                "ITkPD": self.result_info["result"],
                "summary": self.result_info["result"],
            }
        }
        # print(self.test_result_dict)

        self.test_result_dict["results"]["localDB"]["startup_grade"] = self.result_info[
            "startup_grade"
        ]
        self.test_result_dict["results"]["ITkPD"]["startup_grade"] = self.result_info[
            "startup_grade"
        ]
        self.test_result_dict["results"]["summary"]["startup_grade"] = self.result_info[
            "startup_grade"
        ]

        self.test_result_dict["results"]["localDB"]["comment"] = self.result_info[
            "comment"
        ]
        self.test_result_dict["results"]["ITkPD"]["comment"] = self.result_info[
            "comment"
        ]
        self.test_result_dict["results"]["summary"]["comment"] = self.result_info[
            "comment"
        ]

        log.info("[Test Result file] " + self.result_info["filename"])

    ###########################################################################################

    def init_ui(self):
        self.initial_wid = initial_SLDO_VI.InitialWindow(self)
        self.update_widget(self.initial_wid)

    def scale_window(self, x, y):
        self.setGeometry(0, 0, x, y)

    def update_widget(self, w):
        self.scale_window(600, 400)
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
