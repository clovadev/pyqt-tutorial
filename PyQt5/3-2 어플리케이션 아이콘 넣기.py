import sys
from PyQt5 import QtWidgets, QtGui


class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hello, world!')
        self.setWindowIcon(QtGui.QIcon('../res/web.png'))
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
