from PyQt5 import QtWidgets
from ui.MainWindow import MainWindow
from workbench import workbench

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())