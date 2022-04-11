from PyQt5.QtGui import QPainter, QColor, QPen, QGradient
from PyQt5.QtWidgets import QApplication, qApp
from PyQt5.QtCore import Qt, pyqtSignal
from pyqt_resource_helper import PyQtResourceHelper
from pyqt_timer import Timer


class TransparentTimer(Timer):
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

    def paintEvent(self, e):
        if self.testAttribute(Qt.WA_TranslucentBackground):
            pass
        else:
            painter = QPainter(self)
            painter.fillRect(self.rect(), QGradient.PremiumDark)
            pen = QPen(QColor('#777777'), 3)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(pen)
            painter.drawRoundedRect(self.rect(), 10.0, 10.0)
        return super().paintEvent(e)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            p = e.pos()
            self.__offset = p
            self.__moving = True
        return super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self.__moving:
            self.move(e.globalPos() - self.__offset)
        return super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        self.__moving = False
        return super().mouseReleaseEvent(e)

    def enterEvent(self, e):
        self.setFixedSize(self.sizeHint().width() + 1, self.sizeHint().height() + 1)
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        return super().leaveEvent(e)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            qApp.exit()
        return super().keyPressEvent(e)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    timer = TransparentTimer()
    timer.show()
    app.exec_()
