from PyQt5 import QtWidgets, QtCore
from homescreen_ui import Ui_MainWindow
from usecases import config_parser, usecase
import sys
import time
from entities import entity
from database import db_read


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.refresh_button.clicked.connect(self.load_data)
        self.ui.exit_button.clicked.connect(self.exit_app)
        self.nt = entity.NewTaskWindow()
        self.ui.new_task_button.clicked.connect(self.nt.new_task)
        self.ui.load_data_progress_indicator.setValue(0)

    def load_data(self):
        try:
            print("Loading data from database....")
            db_name, db_table_name, db_location = usecase.db_access()
            data = db_read.read_data(db_location + db_name, db_table_name)
            for i in range(0, 101):
                time.sleep(0.05)
                self.ui.load_data_progress_indicator.setValue(i)
            print("Loading complete.")
            print("data:", data)
        except Exception as e:
            print("Exception occurred while loading data from the database!!")
            print("Exception:", e)

    @staticmethod
    def exit_app():
        print("Exiting the application....")
        sys.exit()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
