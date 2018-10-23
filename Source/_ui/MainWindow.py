# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,  QFileDialog,  QMessageBox

from .Ui_MainWindow import Ui_MainWindow

import logging

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    from _workbench import configs
    config_obj = configs.configs()
    global fileName
    fileName = None
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
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        global startID
        startID = int(p0)

    @pyqtSlot(str)
    def on_lineEdit_religion_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        global religion
        religion = p0

    @pyqtSlot(str)
    def on_lineEdit_culture_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        global culture
        culture = p0

    @pyqtSlot(str)
    def on_lineEdi_terrain_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        global terrain
        terrain = p0


    @pyqtSlot(int)
    def on_spinBox_r_valueChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type int
        """
        global rgb_basis_r
        rgb_basis_r = p0

    @pyqtSlot(int)
    def on_spinBox_g_valueChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type int
        """
        global rgb_basis_g
        rgb_basis_g = p0

    @pyqtSlot(int)
    def on_spinBox_b_valueChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type int
        """
        global rgb_basis_b
        rgb_basis_b = p0

    @pyqtSlot(int)
    def on_spinBox_templedist_valueChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type int
        """
        pass

    @pyqtSlot(bool)
    def on_checkBox_isTribal_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        global is_tribal
        is_tribal = checked

    @pyqtSlot(bool)
    def on_checkBox_flagremoval_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        pass

    @pyqtSlot(bool)
    def on_checkBox_baronyhistoryfiles_toggled(self, checked):
        """
        Slot documentation goes here.

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
        logging.info('Loaded File %s',str(fileName))

    @pyqtSlot()
    def on_pushButton_write_pressed(self):
        """
        Write files
        """
        from _workbench import workbench
        import random
        global rgb_basis
        logging.info('Started Writing')
        rgb_basis = list((rgb_basis_r, rgb_basis_g, rgb_basis_b))
        if fileName is None:
            QMessageBox.information(self, "Error", "No File Loaded")
            return
        else:
            logging.info('Parameters: startID=%d Culture=%s Religion=%s Terrain=%s is_tribal=%s rgb_base=%s', startID, culture, religion, terrain, str(is_tribal), rgb_basis)
            workbench.execute.write(fileName[0],startID,culture,religion,is_tribal,terrain,rgb_basis)
            logging.info('----- Exited Writing - ')
            deus_vult_mode = random.randrange(0,15)
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
            config_obj = configs.configs()
            last_file_id = config_obj.read_config('Last_Setup','Last_File_ID')
            last_file_id_int: int = int(last_file_id)
            last_file_id_int += 1
            last_file_id = str(last_file_id_int)
            config_obj.edit_config('Last_Setup','Last_File_ID',str(last_file_id))
            config_obj.edit_config('Last_Setup','startid',str(startID))
            config_obj.edit_config('Last_Setup','culture',culture)
            config_obj.edit_config('Last_Setup','religion',religion)
            config_obj.edit_config('Last_Setup','terrain',terrain)
            config_obj.edit_config('Last_Setup','is_tribal',str(is_tribal))
            config_obj.edit_config('Last_Setup','rgb_basis',str(rgb_basis))
            logging.info('EXECUTION COMPLETE')
            logging.info("-------------------------------------------------------------------------------------------------------------------------------------------------")