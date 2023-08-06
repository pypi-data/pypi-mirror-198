from __future__ import annotations

import logging

from PyQt5.QtWidgets import QMainWindow

from module_qc_nonelec_gui.qc_tests.ivcurve.lib import initial_Sensor_IV

log = logging.getLogger(__name__)


class TestWindow(QMainWindow):
    ############################################################################################
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__()
        self.parent = parent

        self.setWindowTitle("Sensor I-V")
        self.scale_window(510, 255)

        self.result_info = {"comment": "", "filename": ""}

    def receive_result(self, result, comment):
        self.parent.testRun["results"]["Metadata"].update(result)
        self.parent.testRun["results"]["comment"] = comment

        varMap = {
            "CURRENT_MEAN": "Current_mean",
            "CURRENT_SIGMA": "Current_sigma",
            "VOLTAGE": "Voltage",
            "TIME": "Time",
            "HUMIDITY": "Humidity",
        }

        for v1, v2 in varMap.items():
            self.parent.testRun["results"]["Measurements"][v1] = [
                dataPoint.get(v2) for dataPoint in result["Sensor_IV"]
            ]

        self.return_result()

    ###########################################################################################

    def init_ui(self):
        self.initial_wid = initial_Sensor_IV.InitialWindow(self)
        self.update_widget(self.initial_wid)

    def scale_window(self, x, y):
        self.setGeometry(0, 0, x, y)

    def update_widget(self, w):
        self.scale_window(425, 255)
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
        self.parent.receive_result(self)
