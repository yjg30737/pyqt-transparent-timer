from PyQt5.QtGui import QPainter, QColor, QPen, QGradient
from PyQt5.QtWidgets import qApp
from PyQt5.QtCore import Qt, pyqtSignal
from pyqt_resource_helper import PyQtResourceHelper
from pyqt_timer import Timer
from pyqt_frameless_window.framelessWindow import FramelessWindow


class TransparentTimer(Timer, FramelessWindow):
    printSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__offset = 0
        self.__moving = False
        self.__initUi()

    def __initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        PyQtResourceHelper.setStyleSheet([self._btnWidget], ['styles/btn_widget.css'])
        PyQtResourceHelper.setStyleSheet([self._timerLbl], ['styles/timer_lbl.css'])

        self.setMouseTracking(True)
        self._btnWidget.setMouseTracking(True)

        self._btnWidget.setMinimumHeight(self._btnWidget.sizeHint().height()*1.2)

        self.setPressToMove(True)

    def paintEvent(self, e):
        if self.testAttribute(Qt.WA_TranslucentBackground):
            pass
        else:
            painter = QPainter(self)
            painter.fillRect(self.rect(), QGradient.PremiumDark)
            pen = QPen(QColor('#777777'), 3)
            painter.setPen(pen)
            painter.drawRect(self.rect())
        return super().paintEvent(e)

    def enterEvent(self, e):
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.repaint()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()
        return super().leaveEvent(e)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            qApp.exit()
        return super().keyPressEvent(e)