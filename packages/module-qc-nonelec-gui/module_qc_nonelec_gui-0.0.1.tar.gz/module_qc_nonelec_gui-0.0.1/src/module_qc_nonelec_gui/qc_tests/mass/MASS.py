from __future__ import annotations

import logging

from PyQt5.QtWidgets import QMainWindow

from module_qc_nonelec_gui.qc_tests.mass.lib import initial_MASS

log = logging.getLogger(__name__)


class TestWindow(QMainWindow):
    ############################################################################################
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__()
        self.parent = parent

        self.setWindowTitle("Mass Measurement")
        self.scale_window(340, 255)

        self.result_info = {
            "Scale_accuracy_value": "",
            "Scale_accuracy_unit": "mg",
            "mass_value": "",
            "mass_unit": "mg",
            "comment": "",
        }

    ###########################################################################################

    def init_ui(self):
        self.initial_wid = initial_MASS.InitialWindow(self)
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

    def receive_mass(self, mass_value, acu_value, comment):
        # Essentially only here is the hard-coded part (value mapping ).
        self.parent.testRun["results"]["Measurements"]["MASS"] = float(mass_value)
        self.parent.testRun["results"]["property"]["SCALE_ACCURACY"] = float(acu_value)
        self.parent.testRun["results"]["comment"] = str(comment)
        self.parent.testRun["results"]["Metadata"]["MASS_UNIT"] = self.result_info[
            "mass_unit"
        ]
        self.parent.testRun["results"]["Metadata"][
            "SCALE_ACCURACY_UNIT"
        ] = self.result_info["Scale_accuracy_unit"]

        self.return_result()

    def return_result(self):
        self.parent.receive_result(self)
