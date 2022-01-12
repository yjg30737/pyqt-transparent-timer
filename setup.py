from setuptools import setup, find_packages

setup(
    name='pyqt-transparent-timer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_transparent_timer.style': ['button.css'], 'pyqt_transparent_timer.ico': ['play.png', 'pause.png', 'stop.png', 'settings.png']},
    description='PyQt transparent timer',
    url='https://github.com/yjg30737/pyqt-transparent-timer.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main',
        'pyqt-notifier @ git+https://git@github.com/yjg30737/pyqt-notifier.git@main'
    ]
)