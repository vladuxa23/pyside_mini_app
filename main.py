from PySide2 import QtCore, QtWidgets, QtGui
from main_form import Ui_Form


class MyApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButtonSend.clicked.connect(self.receive_message)

    def receive_message(self):
        print(f"Имя: {self.ui.lineEditName.text()}")
        print(f"Телефон: {self.ui.lineEditPhone.text()}")

        self.ui.lineEditName.clear()
        self.ui.lineEditPhone.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = MyApp()
    win.show()
    app.exec_()
