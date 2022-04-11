from setuptools import setup, find_packages

setup(
    name='pyqt-transparent-timer',
    version='0.3.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_transparent_timer.styles': ['btn_widget.css', 'timer_lbl.css']},
    description='PyQt transparent timer',
    url='https://github.com/yjg30737/pyqt-transparent-timer.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-timer @ git+https://git@github.com/yjg30737/pyqt-timer.git@main',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)