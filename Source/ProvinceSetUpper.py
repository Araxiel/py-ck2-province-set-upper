from PyQt5 import QtWidgets
from _ui.MainWindow import MainWindow
from _workbench import auxiliary

if __name__ == '__main__':
    import sys
    auxiliary.log.logging_init()
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())