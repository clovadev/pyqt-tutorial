import sys
from PyQt5 import QtWidgets


class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 300)

        qrect = self.frameGeometry()
        centerpoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qrect.moveCenter(centerpoint)

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
