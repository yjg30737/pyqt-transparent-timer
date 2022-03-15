from setuptools import setup, find_packages

setup(
    name='pyqt-transparent-timer',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_transparent_timer.ico': ['play.svg', 'pause.svg', 'stop.svg', 'settings.svg']},
    description='PyQt transparent timer',
    url='https://github.com/yjg30737/pyqt-transparent-timer.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-notifier @ git+https://git@github.com/yjg30737/pyqt-notifier.git@main',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main',
        'pyqt-timer @ git+https://git@github.com/yjg30737/pyqt-timer.git@main'
    ]
)