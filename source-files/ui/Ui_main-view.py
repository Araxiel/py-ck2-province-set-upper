# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Paradox Interactive\Crusader Kings II\Modding\Province Set-Upper\source-files\ui\main-view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 405)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 12, 431, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_load = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.gridLayout.addWidget(self.pushButton_load, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_config = QtWidgets.QWidget()
        self.tab_config.setObjectName("tab_config")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_config)
        self.splitter_2.setGeometry(QtCore.QRect(11, 20, 201, 91))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_religion = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_religion.setText("")
        self.lineEdit_religion.setObjectName("lineEdit_religion")
        self.horizontalLayout.addWidget(self.lineEdit_religion)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_culture = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_culture.setText("")
        self.lineEdit_culture.setClearButtonEnabled(False)
        self.lineEdit_culture.setObjectName("lineEdit_culture")
        self.horizontalLayout_2.addWidget(self.lineEdit_culture)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_rgb = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_rgb.setText("")
        self.lineEdit_rgb.setObjectName("lineEdit_rgb")
        self.horizontalLayout_3.addWidget(self.lineEdit_rgb)
        self.tabWidget.addTab(self.tab_config, "")
        self.tab_preview = QtWidgets.QWidget()
        self.tab_preview.setObjectName("tab_preview")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_preview)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(self.tab_preview)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_preview, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_output_location = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_output_location.setObjectName("lineEdit_output_location")
        self.horizontalLayout_4.addWidget(self.lineEdit_output_location)
        self.pushButton_write = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_write.setEnabled(True)
        self.pushButton_write.setObjectName("pushButton_write")
        self.horizontalLayout_4.addWidget(self.pushButton_write)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 458, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionGenerate_Empty_File = QtWidgets.QAction(MainWindow)
        self.actionGenerate_Empty_File.setObjectName("actionGenerate_Empty_File")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionGenerate_Empty_File)
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Province Set-Upper"))
        self.pushButton_load.setText(_translate("MainWindow", "Load"))
        self.label_2.setText(_translate("MainWindow", "Religion:"))
        self.lineEdit_religion.setToolTip(_translate("MainWindow", "<html><head/><body><p>The default culture of all provinces</p></body></html>"))
        self.lineEdit_religion.setPlaceholderText(_translate("MainWindow", "Catholic"))
        self.label.setText(_translate("MainWindow", "Culture:"))
        self.lineEdit_culture.setToolTip(_translate("MainWindow", "<html><head/><body><p>The default culture of all provinces</p></body></html>"))
        self.lineEdit_culture.setPlaceholderText(_translate("MainWindow", "Norse"))
        self.label_3.setText(_translate("MainWindow", "RGB Base:"))
        self.lineEdit_rgb.setPlaceholderText(_translate("MainWindow", "179 222 112"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), _translate("MainWindow", "Config"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_preview), _translate("MainWindow", "Preview"))
        self.pushButton_write.setText(_translate("MainWindow", "Write"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionGenerate_Empty_File.setText(_translate("MainWindow", "Generate Empty File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
