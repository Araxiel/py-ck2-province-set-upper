# -*- coding: utf-8 -*-

"""
Module implementing AboutUI.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_About import Ui_AboutUI


class AboutUI(QDialog, Ui_AboutUI):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(AboutUI, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_exit_pressed(self):
        self.close()
