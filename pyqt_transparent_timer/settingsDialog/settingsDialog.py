
from PyQt5 import Qt
from PyQt5.QtWidgets import QDialog, QTabWidget, QVBoxLayout, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt

from pyqt_transparent_timer.settingsDialog.timerSettingsWidget.timerSettingsWidget import TimerSettingsWidget


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Settings')
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)

        self.__timerSettingsWidget = TimerSettingsWidget()

        topWidget = QTabWidget()
        topWidget.addTab(self.__timerSettingsWidget, 'Timer')

        self.__okBtn = QPushButton()
        self.__okBtn.clicked.connect(self.accept)
        self.__okBtn.setText('OK')

        closeBtn = QPushButton()
        closeBtn.clicked.connect(self.close)
        closeBtn.setText('Cancel')

        lay = QHBoxLayout()
        lay.addWidget(self.__okBtn)
        lay.addWidget(closeBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(bottomWidget)
        self.setLayout(lay)

    def __ok(self):
        self.accept()

    def get_time(self):
        return self.__timerSettingsWidget.get_time()