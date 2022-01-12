from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


class TimerLabel(QWidget):
    doubleClicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        self.__lbl = QLabel('00:00:00')
        self.__lbl.setAlignment(Qt.AlignCenter)
        self.__lbl.setFont(QFont('Arial', 24))
        self.__lbl.setStyleSheet('QLabel { color: white; }')
        lay = QGridLayout()
        lay.addWidget(self.__lbl)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def setText(self, text):
        self.__lbl.setText(text)

    def mouseDoubleClickEvent(self, e):
        self.doubleClicked.emit()
