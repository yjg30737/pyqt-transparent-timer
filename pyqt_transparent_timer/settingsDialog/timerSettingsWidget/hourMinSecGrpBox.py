from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QGroupBox, QSpinBox, QSizePolicy, QFormLayout


class HourMinSecGrpBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.__settings_struct = QSettings('timerSettings.ini', QSettings.IniFormat)
        self.__hour = int(self.__settings_struct.value('hour', 0))
        self.__min = int(self.__settings_struct.value('min', 0))
        self.__sec = int(self.__settings_struct.value('sec', 0))
        self.__initUi()

    def __initUi(self):
        self.__hourSpinBox = QSpinBox()
        self.__minSpinBox = QSpinBox()
        self.__secSpinBox = QSpinBox()
        
        self.__hourSpinBox.setValue(self.__hour)
        self.__minSpinBox.setValue(self.__min)
        self.__secSpinBox.setValue(self.__sec)

        self.__hourSpinBox.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.__minSpinBox.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.__secSpinBox.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        self.__minSpinBox.setRange(0, 59)
        self.__secSpinBox.setRange(0, 59)

        self.__hourSpinBox.valueChanged.connect(self.__hourChanged)
        self.__minSpinBox.valueChanged.connect(self.__minChanged)
        self.__secSpinBox.valueChanged.connect(self.__secChanged)

        lay = QFormLayout()
        lay.addRow('Hour', self.__hourSpinBox)
        lay.addRow('Minute', self.__minSpinBox)
        lay.addRow('Second', self.__secSpinBox)

        self.setLayout(lay)
        self.setTitle('H/M/S Settings')

    def __hourChanged(self):
        self.__hour = self.__hourSpinBox.value()

    def __minChanged(self):
        self.__min = self.__minSpinBox.value()

    def __secChanged(self):
        self.__sec = self.__secSpinBox.value()

    def get_hour(self):
        return self.__hour

    def get_min(self):
        return self.__min

    def get_sec(self):
        return self.__sec