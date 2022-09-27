import datetime
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class StopWatchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seconds")
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # <MainWindow Properties>
        self.setFixedSize(300, 50)
        self.center()
        # </MainWindow Properties>

        self.second = '00'

        # <Label Properties>
        self.lbl = QLabel(self)
        self.lbl.setText("test")
        self.lbl.setMinimumHeight(50)
        self.lbl.setMinimumWidth(300)
        self.lbl.setAlignment(Qt.AlignCenter)
        # </Label Properties>

        timer = QTimer(self)
        timer.timeout.connect(self.showCounter)
        timer.start(100)
        sizeObject = QDesktopWidget().screenGeometry(-1)

        self.move(sizeObject.width() - 300, 0)

        self.oldPos = self.pos()

    def showCounter(self):

        self.now = datetime.datetime.now()
        self.midnight = self.now.replace(hour=0, minute=0, second=0, microsecond=0)
        self.second = str(86400 - (self.now - self.midnight).seconds)

        text = self.second + " left"
        # Display the stop watch values in the label
        self.lbl.setText(text)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('src/Montserrat.ttf')
    stylesheet = open('src/mystylesheet.qss').read()
    app.setStyleSheet(stylesheet)
    stopWt = StopWatchWindow()
    stopWt.show()
    sys.exit(app.exec_())
