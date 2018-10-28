from PyQt5 import QtWidgets
from _ui.MainWindow import MainWindow

if __name__ == '__main__':
    import sys
    import logging
    from _workbench import configs
    configs_obj = configs.configs()
    logging.basicConfig(filename='setupper.log', filemode='w+', format='%(levelname)s %(asctime)s: [ %(message)s ]',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info('Set-Upper Started')
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
