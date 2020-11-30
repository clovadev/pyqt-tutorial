import sys
from PyQt5 import QtWidgets

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready', 5000)

        button1 = QtWidgets.QPushButton('clearMessage', self)
        button1.clicked.connect(self.statusBar().clearMessage)
        button1.move(200, 100)
        button1.resize(button1.sizeHint())

        self.setWindowTitle('Statusbar')
        self.setGeometry(1000, 500, 500, 300)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
