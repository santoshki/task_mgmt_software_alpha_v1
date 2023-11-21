import new_task_ui
from usecases import usecase
from PyQt5 import QtWidgets, QtCore
from database import db_insert


class NewTaskWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(NewTaskWindow, self).__init__()
        self.window = QtWidgets.QMainWindow()
        self.ui = new_task_ui.Ui_MainWindow()
        self.ui.setupUi(self)

    def new_task(self):
        try:
            print("Opening New task window....")
            self.window = QtWidgets.QMainWindow()
            self.ui = new_task_ui.Ui_MainWindow()
            self.ui.setupUi(self.window)
            taskid = usecase.generate_taskid()
            self.ui.task_id_value.setPlainText(taskid)
            self.ui.task_id_value.setEnabled(False)
            self.ui.task_state_dropdown.addItems({"New"})
            self.ui.task_priority_dropdown.addItems({"Low", "Medium", "High", "Critical"})
            self.ui.timestamp_value.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui.timestamp_value.setEnabled(False)
            self.window.show()
            self.ui.back_button.clicked.connect(self.back)
            self.ui.reset_values_button.clicked.connect(self.reset_values)
            self.ui.create_task_button.clicked.connect(self.create_task)
        except Exception as e:
            raise Exception("Error occurred while opening new task window screen:", e)

    def back(self):
        print("Back button pressed, closing current display screen...")
        self.window.close()

    def reset_values(self):
        try:
            print("Reset values button pressed.\nResetting the field values...")
            self.ui.assigned_to_value.setPlainText("")
            self.ui.task_description_value.setPlainText("")
            self.ui.task_title_value.setPlainText("")
            self.ui.notes_value.setPlainText("")
            self.ui.task_priority_dropdown.setCurrentIndex(0)
        except Exception as e:
            raise Exception("Error occurred while resetting form values:", e)

    def create_task(self):
        try:
            new_task_details = []
            print("Capturing new task details......")
            task_id_value = self.ui.task_id_value.toPlainText()
            task_title_value = self.ui.task_title_value.toPlainText()
            task_description_value = self.ui.task_description_value.toPlainText()
            task_state_dropdown_value = self.ui.task_state_dropdown.currentText()
            task_notes_value = self.ui.notes_value.toPlainText()
            task_priority_value = self.ui.task_priority_dropdown.currentText()
            task_assigned_to_value = self.ui.assigned_to_value.toPlainText()
            task_created_timestamp_value = self.ui.timestamp_value.dateTime()
            task_created_timestamp_value = task_created_timestamp_value.toString()
            if task_title_value == "":
                print("Task title cannot be empty!")
            elif task_description_value == "":
                print("Task description cannot be empty!")
            else:
                new_task_details = [task_id_value, task_title_value, task_description_value, task_state_dropdown_value,
                                    task_notes_value, task_priority_value, task_assigned_to_value,
                                    task_created_timestamp_value]
                print("New task details captured")
                print("Task details:", new_task_details)
                db_insert.insert_data("C:\\Users\\santosh.a.d.kulkarni\\PycharmProjects\\task_mgmt_software_alpha_v1"
                                      "\\database\\new_task", "task", new_task_details)
                self.window.close()
        except Exception as e:
            raise Exception("Exception occurred while saving the new task:", e)
