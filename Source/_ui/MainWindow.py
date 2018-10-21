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
    global fileName
    fileName = None
    global startID
    startID = 16
    global culture
    culture = "Norse"
    global religion
    religion = "Catholic"
    global is_tribal
    is_tribal = False
    global terrain
    terrain = "Plains"
    global rgb_basis
    rgb_basis = list((255, 105, 0))
    global rgb_basis_r
    rgb_basis_r = 255
    global rgb_basis_g
    rgb_basis_g = 105
    global rgb_basis_b
    rgb_basis_b = 0
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
    
    @pyqtSlot(bool)
    def on_checkBox_isTribal_toggled(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        global is_tribal
        is_tribal = checked

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
            logging.info('Complete')
            logging.info("-------------------------------------------------------------------------------------------------------------------------------------------------")