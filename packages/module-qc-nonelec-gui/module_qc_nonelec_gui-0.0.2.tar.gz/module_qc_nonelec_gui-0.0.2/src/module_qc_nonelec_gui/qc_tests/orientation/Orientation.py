from __future__ import annotations

import logging

from PyQt5.QtWidgets import QMainWindow

from module_qc_nonelec_gui.qc_tests.orientation.lib import initial_Orientation

log = logging.getLogger(__name__)


class TestWindow(QMainWindow):
    ############################################################################################
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__()
        self.parent = parent

        self.setWindowTitle("Orientation")
        self.scale_window(340, 255)

        self.result_info = {"comment": ""}

    def receive_result(self, isTrue, comment):
        self.result_info["orientation"] = isTrue
        self.result_info["comment"] = comment

        self.fill_result()
        self.return_result()

    def fill_result(self):
        self.test_result_dict = {
            "results": {
                "localDB": {
                    "orientation": self.result_info["orientation"],
                    "comment": self.result_info["comment"],
                },
                "ITkPD": {
                    "orientation": self.result_info["orientation"],
                    "comment": self.result_info["comment"],
                },
                "summary": {
                    "orientation": self.result_info["orientation"],
                    "comment": self.result_info["comment"],
                },
            }
        }
        log.info(
            "[Test Result] orientation is "
            + str(self.test_result_dict["results"]["localDB"]["orientation"])
        )

    ###########################################################################################

    def init_ui(self):
        self.initial_wid = initial_Orientation.InitialWindow(self)
        self.update_widget(self.initial_wid)

    def scale_window(self, x, y):
        self.setGeometry(0, 0, x, y)

    def update_widget(self, w):
        self.scale_window(340, 255)
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
