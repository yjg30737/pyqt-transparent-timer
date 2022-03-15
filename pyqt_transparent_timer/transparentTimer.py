from PyQt5.QtGui import QPainter, QColor, QPen, QGradient
from PyQt5.QtWidgets import QWidget, QApplication, \
    QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QSizePolicy, qApp
from PyQt5.QtCore import Qt, pyqtSignal, QTime, QTimer, QSettings
from pyqt_notifier import NotifierWidget
from pyqt_resource_helper import PyQtResourceHelper

from pyqt_transparent_timer import TimerLabel
from pyqt_transparent_timer.settingsDialog import SettingsDialog


class TransparentTimer(QWidget):
    printSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__settings_struct = QSettings('timerSettings.ini', QSettings.IniFormat)
        self.__hour = int(self.__settings_struct.value('hour', 0))
        self.__min = int(self.__settings_struct.value('min', 0))
        self.__sec = int(self.__settings_struct.value('sec', 0))

        self.__offset = 0
        self.__moving = False
        self.__initUi()

    def __initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.__timer_lbl = TimerLabel()
        self.__timer_lbl.doubleClicked.connect(self.__settings)

        self.__startPauseBtn = QPushButton()
        self.__stopBtn = QPushButton()
        self.__settingsBtn = QPushButton()

        self.__startPauseBtn.setToolTip('Start')
        self.__stopBtn.setToolTip('Stop')
        self.__settingsBtn.setToolTip('Settings')

        btns = [self.__startPauseBtn, self.__stopBtn, self.__settingsBtn]

        PyQtResourceHelper.setStyleSheet(btns, ['style/button.css'])
        PyQtResourceHelper.setIcon(btns, ['ico/play.png', 'ico/stop.png', 'ico/settings.png'])

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        for btn in btns:
            lay.addWidget(btn)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        btnWidget = QWidget()
        btnWidget.setLayout(lay)
        btnWidget.setStyleSheet('QWidget { '
                                'border: 1px solid #444; '
                                'padding: 5px; '
                                'border-radius: 5px; '
                                'background-color: #888888;}'
                                )

        btnWidget.setMinimumWidth(btnWidget.sizeHint().width()*1.5)
        btnWidget.setMinimumHeight(btnWidget.sizeHint().height()*1.5)

        lay = QVBoxLayout()
        lay.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        lay.addWidget(self.__timer_lbl)
        lay.addWidget(btnWidget)
        self.setMouseTracking(True)

        self.setLayout(lay)

        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())

        self.__timerInit()

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

    def __timerInit(self):
        self.__startPauseBtn.setObjectName('start')

        self.__startPauseBtn.clicked.connect(self.__start)
        self.__stopBtn.clicked.connect(self.__stop)
        self.__settingsBtn.clicked.connect(self.__settings)

        self.__taskTimeLeft = QTime(self.__hour, self.__min, self.__sec)
        self.__timer = QTimer(self)

        self.__startPauseBtn.setEnabled(False)
        self.__stopBtn.setEnabled(False)

    def __start(self):
        try:
            if self.__startPauseBtn.objectName() == 'start':
                # adding action to timer
                self.__timer.timeout.connect(self.__timer_ticking)
                self.__timer.singleShot(self.__taskTimeLeft.msec(), self.__prepare_to_timer)
                # update the timer every second
                self.__timer.start(1000)
                self.__startPauseBtn.setObjectName('pause')
                PyQtResourceHelper.setIcon([self.__startPauseBtn], ['ico/pause.png'])
                self.__startPauseBtn.clicked.connect(self.__pause_and_restart)

                self.__stopBtn.setEnabled(True)
        except Exception as e:
            print(e)
            print(sys.exc_info()[2].tb_lineno)
            print(sys.exc_info())

    def __prepare_to_timer(self):
        self.__settingsBtn.setEnabled(False)
        self.__timer_lbl.doubleClicked.disconnect(self.__settings)
        self.__timer_ticking()

    def __pause_and_restart(self):
        try:
            if self.__startPauseBtn.objectName() == 'pause':
                self.__timer.stop()
                PyQtResourceHelper.setIcon([self.__startPauseBtn], ['ico/play.png'])
                self.__startPauseBtn.setObjectName('restart')
            elif self.__startPauseBtn.objectName() == 'restart':
                self.__timer.start()
                PyQtResourceHelper.setIcon([self.__startPauseBtn], ['ico/pause.png'])
                self.__startPauseBtn.setObjectName('pause')
        except Exception as e:
            print(e)

    def __notify_times_up(self):
        self.__notifier = NotifierWidget('Notice', 'Times up.')
        refreshBtn = QPushButton('Restart')
        refreshBtn.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        refreshBtn.clicked.connect(self.__start)
        self.__notifier.addWidgets([refreshBtn])
        self.__notifier.show()

    def __timer_ticking(self):
        try:
            self.__taskTimeLeft = self.__taskTimeLeft.addSecs(-1)
            time_left_text = self.__taskTimeLeft.toString('hh:mm:ss')
            self.__timer_lbl.setText(time_left_text)
            if '23:59:59' == time_left_text:
                self.__notify_times_up()
                self.__stop()
            else:
                pass
        except Exception as e:
            print(e)
            print(sys.exc_info()[2].tb_lineno)
            print(sys.exc_info())

    def __stop(self):
        try:
            self.__taskTimeLeft = QTime(self.__hour, self.__min, self.__sec)
            self.__timer_lbl.setText(self.__taskTimeLeft.toString("hh:mm:ss"))

            self.__timer.stop()

            self.__startPauseBtn.setObjectName('start')
            PyQtResourceHelper.setIcon([self.__startPauseBtn], ['ico/play.png'])

            self.__timer.timeout.disconnect(self.__timer_ticking)
            self.__startPauseBtn.clicked.disconnect(self.__pause_and_restart)
            self.__startPauseBtn.clicked.connect(self.__start)

            self.__settingsBtn.setEnabled(True)
            self.__stopBtn.setEnabled(False)

            self.__timer_lbl.doubleClicked.connect(self.__settings)

        except Exception as e:
            print(e)
            print(sys.exc_info()[2].tb_lineno)
            print(sys.exc_info())

    def __settings(self):
        print('settings')
        dialog = SettingsDialog()
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            self.__hour, self.__min, self.__sec = dialog.get_time()

            self.__taskTimeLeft = QTime(self.__hour, self.__min, self.__sec)
            task_time_text = self.__taskTimeLeft.toString('hh:mm:ss')

            self.__timer_lbl.setText(task_time_text)
            self.__startPauseBtn.setEnabled(task_time_text != '00:00:00')

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
