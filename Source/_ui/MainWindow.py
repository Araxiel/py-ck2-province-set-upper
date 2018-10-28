# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from .Ui_MainWindow import Ui_MainWindow

import logging


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    from _workbench import configs
    config_obj = configs.configs()
    #   ---- fileName
    global fileName
    fileName_str = config_obj.read_config('Last_Setup', 'Last_fileName')
    if fileName_str in ['None'] or fileName_str in '':
        fileName = None
    else:
        fileName = fileName_str
        from pathlib import Path
        my_file = Path(fileName)
        if not my_file.is_file():
            fileName = None
            config_obj.edit_config('Last_Setup', 'Last_fileName', 'None')
    #   ---- fileName End
    global startID
    startID_str = config_obj.read_config('Last_Setup', 'startID')
    startID = int(startID_str)
    global culture
    culture = config_obj.read_config('Last_Setup', 'culture')
    global religion
    religion = config_obj.read_config('Last_Setup', 'religion')
    global is_tribal
    is_tribal_str = config_obj.read_config('Last_Setup', 'is_tribal')
    if is_tribal_str in ['true']:
        is_tribal = True
    else:
        is_tribal = False
    global terrain
    terrain = config_obj.read_config('Last_Setup', 'terrain')
    global rgb_basis
    rgb_basis_listl = config_obj.read_config('Last_Setup', 'rgb_basis')
    import ast
    rgb_basis = ast.literal_eval(rgb_basis_listl)
    global rgb_basis_r
    rgb_basis_r = rgb_basis[0]
    global rgb_basis_g
    rgb_basis_g = rgb_basis[1]
    global rgb_basis_b
    rgb_basis_b = rgb_basis[2]
    global flag_removal
    flag_removal = False

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot(str)
    def on_lineEdit_startID_textChanged(self, p0):
        """
        @param p0 DESCRIPTION
        @type str
        """
        global startID
        startID = int(p0)

    @pyqtSlot(str)
    def on_lineEdit_religion_textChanged(self, p0):
        """
        @param p0 DESCRIPTION
        @type str
        """
        global religion
        religion = p0

    @pyqtSlot(str)
    def on_lineEdit_culture_textChanged(self, p0):
        """
        @param p0 DESCRIPTION
        @type str
        """
        global culture
        culture = p0

    @pyqtSlot(str)
    def on_lineEdi_terrain_textChanged(self, p0):
        """
        @param p0 DESCRIPTION
        @type str
        """
        global terrain
        terrain = p0

    @pyqtSlot(int)
    def on_spinBox_r_valueChanged(self, p0):
        """
        @param p0 DESCRIPTION
        @type int
        """
        global rgb_basis_r
        rgb_basis_r = p0

    @pyqtSlot(int)
    def on_spinBox_g_valueChanged(self, p0):
        """
        @param p0 DESCRIPTION
        @type int
        """
        global rgb_basis_g
        rgb_basis_g = p0

    @pyqtSlot(int)
    def on_spinBox_b_valueChanged(self, p0):
        """
        @param p0 DESCRIPTION
        @type int
        """
        global rgb_basis_b
        rgb_basis_b = p0

    @pyqtSlot(int)
    def on_spinBox_templedist_valueChanged(self, p0):
        """
        @param p0 DESCRIPTION
        @type int
        """
        pass

    @pyqtSlot(bool)
    def on_checkBox_isTribal_toggled(self, checked):
        """
        @param checked DESCRIPTION
        @type bool
        """
        global is_tribal
        is_tribal = checked

    @pyqtSlot(bool)
    def on_checkBox_flagremoval_toggled(self, checked):
        """
        @param checked DESCRIPTION
        @type bool
        """
        global flag_removal
        flag_removal = checked

    @pyqtSlot(bool)
    def on_checkBox_baronyhistoryfiles_toggled(self, checked):
        """
        @param checked DESCRIPTION
        @type bool
        """
        pass

    @pyqtSlot()
    def on_actionConfig_triggered(self):
        import os
        os.startfile('config.ini')

    @pyqtSlot()
    def on_actionQuit_triggered(self):
        logging.info('Quit')
        self.close()

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        logging.info('About')
        from _ui.About import AboutUI
        ui = AboutUI()
        ui.exec_()

    @pyqtSlot()
    def on_actionHelp_triggered(self):
        logging.info('Help')
        import webbrowser
        webbrowser.open('https://goo.gl/RDSgwA')  # Go to example.com

    @pyqtSlot()
    def on_pushButton_load_pressed(self):
        """
        Load file
        """
        global fileName
        fileName = QFileDialog.getOpenFileName(
            self,
            self.tr("Load Provinces File"),
            "",
            self.tr("*.csv;;*"),
            self.tr(".csv"))
        fileName = fileName[0]
        logging.info('Loaded File %s', str(fileName))

    @pyqtSlot()
    def on_pushButton_write_pressed(self):
        """
        Writing everything.
        """
        from _workbench import workbench
        import random
        global rgb_basis
        from _workbench import configs
        config_obj = configs.configs()
        last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
        current_version = config_obj.read_config('Basic', 'Version')
        username = config_obj.read_config('Basic', 'User')
        logging.info('Started Writing   ~~  Version: %s   ~~  User: %s  ~~  Run ID: %s', current_version, username, last_file_id)
        rgb_basis = list((rgb_basis_r, rgb_basis_g, rgb_basis_b))
        if fileName is None or fileName is '':
            QMessageBox.critical(
                self,
                self.tr("No File"),
                self.tr("""No file has been loaded.\nYou need to first load a file."""),
                QMessageBox.StandardButtons(
                    QMessageBox.Cancel))
            return
        else:
            logging.info('Parameters: startID=%d Culture=%s Religion=%s Terrain=%s is_tribal=%s rgb_base=%s', startID,
                         culture, religion, terrain, str(is_tribal), rgb_basis)
            if flag_removal is True:
                logging.info('Flag Removal turned on')
                enough_flags_check = workbench.province.read.flags.check_if_enough(fileName)
                if enough_flags_check is False:
                    QMessageBox.critical(
                        self,
                        self.tr("Not Enough Flags"),
                        self.tr("""Flag Removal is selected, but there are more provinces than there are flags in the folder."""),
                        QMessageBox.StandardButtons(
                            QMessageBox.Cancel))
                    logging.info('~~~ Aborted: Not enough flags in folder.')
                    return
                else:
                    import os
                    psueod_flag_log_rel_path = "Databases\\Flags\\Removed\\"
                    pseudo_log_path = psueod_flag_log_rel_path + 'removed_flag_list.log'
                    os.makedirs(os.path.dirname(pseudo_log_path), exist_ok=True)  # create folder
                    with open(pseudo_log_path, "w+") as file:
                        file.write("~~~~~~~~~~~~~~\nFor run ID %s\n" % (last_file_id))
                    pass
            workbench.execute.write(fileName, startID, culture, religion, is_tribal, terrain, rgb_basis,
                                    flag_removal)
            logging.info('----- Exited Writing ----- ')
            deus_vult_mode = random.randrange(0, 15)
            if deus_vult_mode < 2:
                logging.info('DEUS VULT')
                print("DEUS VULT INFIDEL")
                for x in range(3):
                    print("DEUS VULT DEUS VULT DEUS VULT")
                import webbrowser
                webbrowser.open('https://webmshare.com/play/ZQDQw')
                for x in range(3):
                    QMessageBox.information(self, "DEUS VULT INFIDEL",
                                            "DEUS VULT DEUS VULT DEUS VULT\nDEUS VULT DEUS VULT DEUS VULT\nDEUS VULT DEUS VULT DEUS VULT\n")
            else:
                QMessageBox.information(self, "Complete", "Complete\n\nCheck the Output folder")
            from _workbench import configs
            logging.info('Writing Config')
            last_file_id_int: int = int(last_file_id)
            last_file_id_int += 1
            last_file_id = str(last_file_id_int)
            config_obj.edit_config('Last_Setup', 'Last_File_ID', str(last_file_id))
            if startID is not '':
                config_obj.edit_config('Last_Setup', 'startid', str(startID))
            if culture is not '':
                config_obj.edit_config('Last_Setup', 'culture', culture)
            if religion is not '':
                config_obj.edit_config('Last_Setup', 'religion', religion)
            if terrain is not '':
                config_obj.edit_config('Last_Setup', 'terrain', terrain)
            config_obj.edit_config('Last_Setup', 'is_tribal', str(is_tribal))
            config_obj.edit_config('Last_Setup', 'rgb_basis', str(rgb_basis))
            config_obj.edit_config('Last_Setup', 'Last_fileName', str(fileName))
            logging.info('EXECUTION COMPLETE')
            logging.info(
                "----------------------------------------------------------------------------------------------------------------------------")
