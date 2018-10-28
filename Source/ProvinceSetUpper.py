from PyQt5 import QtWidgets
from _ui.MainWindow import MainWindow
import logging
logging.basicConfig(filename='setupper.log', filemode='w', format='%(levelname)s %(asctime)s: [ %(message)s ]', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

if __name__ == '__main__':
    import sys
    logging.info('Set-Upper Started')
    from _workbench import configs
    configs_obj = configs.configs()
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())