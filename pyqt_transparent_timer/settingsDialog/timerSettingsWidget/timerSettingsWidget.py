from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from pyqt_transparent_timer.settingsDialog.timerSettingsWidget.hourMinSecGrpBox import HourMinSecGrpBox


class TimerSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__settings_struct = QSettings('timerSettings.ini', QSettings.IniFormat)
        self.__initUi()

    def __initUi(self):
        self.__hourMinSecGrpBox = HourMinSecGrpBox()

        lay = QHBoxLayout()
        lay.addWidget(self.__hourMinSecGrpBox)
        self.setLayout(lay)

    def get_time(self):
        hour = self.__hourMinSecGrpBox.get_hour()
        min = self.__hourMinSecGrpBox.get_min()
        sec = self.__hourMinSecGrpBox.get_sec()
        self.__settings_struct.setValue('hour', hour)
        self.__settings_struct.setValue('min', min)
        self.__settings_struct.setValue('sec', sec)
        self.__settings_struct.sync()
        return hour, min, sec

