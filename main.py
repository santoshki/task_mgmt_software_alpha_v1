from PyQt5 import QtWidgets
from homescreen_ui import Ui_MainWindow
import sys
import time


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.refresh_button.clicked.connect(self.load_data)
        self.ui.exit_button.clicked.connect(self.exit_app)

    @staticmethod
    def exit_app():
        print("Exiting the application....")
        sys.exit()

    def load_data(self):
        try:
            print("Loading data from database....")
            for i in range(0, 101):
                time.sleep(0.05)
                self.ui.load_data_progress_indicator.setValue(i)
            print("Loading complete.")
        except Exception as e:
            print("Exception occurred while loading data from the database!!")
            print("Exception:", e)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
