# pyqt-transparent-timer
PyQt transparent timer

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-transparent-timer.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-notifier.git">pyqt-notifier</a>
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Usage
* Press the escape button if you want to quit.
* If you want to know more, see <a href="https://github.com/yjg30737/pyqt-timer/blob/main/README.md">README of pyqt-timer</a>

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_transparent_timer import TransparentTimer


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    tm = TransparentTimer()
    tm.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/149067604-650f7927-5470-44a2-b505-c863e28d8237.png)

When mouse cursor is hovering over the widget, border and background will show up.

![image](https://user-images.githubusercontent.com/55078043/149068105-d399fa18-1e48-4556-9d29-90c4f7a3e53e.png)

Except for graphics, this module operates the same way as pyqt-timer.

## See also
<a href="https://github.com/yjg30737/pyqt-timer.git">pyqt-timer</a>
