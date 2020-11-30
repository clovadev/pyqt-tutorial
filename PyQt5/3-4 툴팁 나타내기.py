import sys
from PyQt5 import QtWidgets, QtGui


class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('이것은 <b>QWidget</b>입니다.')

        button = QtWidgets.QPushButton('Quit', self)
        button.setToolTip('이것은 <b>QPushButton</b>입니다.')
        button.move(100, 100)

        self.setWindowTitle('Hello, world!')
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
