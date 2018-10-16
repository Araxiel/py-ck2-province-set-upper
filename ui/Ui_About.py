# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Paradox Interactive\Crusader Kings II\Modding\Province Set-Upper Eric\ui\About.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutUI(object):
    def setupUi(self, AboutUI):
        AboutUI.setObjectName("AboutUI")
        AboutUI.resize(245, 423)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutUI.sizePolicy().hasHeightForWidth())
        AboutUI.setSizePolicy(sizePolicy)
        AboutUI.setAccessibleName("")
        AboutUI.setAccessibleDescription("")
        AboutUI.setSizeGripEnabled(False)
        self.splitter_2 = QtWidgets.QSplitter(AboutUI)
        self.splitter_2.setGeometry(QtCore.QRect(10, 10, 228, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setMaximumSize(QtCore.QSize(228, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setLineWidth(2)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(5)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_exit = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        self.pushButton_exit.setMaximumSize(QtCore.QSize(80, 23))
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.retranslateUi(AboutUI)
        QtCore.QMetaObject.connectSlotsByName(AboutUI)

    def retranslateUi(self, AboutUI):
        _translate = QtCore.QCoreApplication.translate
        AboutUI.setWindowTitle(_translate("AboutUI", "About"))
        self.label_2.setText(_translate("AboutUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CK2 Province Set-Upper</span></p></body></html>"))
        self.label_3.setText(_translate("AboutUI", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">The Province Set-Upper is a small utility to make map-creating less of a tedious chore. </span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Written for CK2 2.8.3.3 (SAHQ)</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Tested with </span><span style=\" font-size:9pt; font-weight:600;\">CK2 2.8.3.3 (SAHQ)</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Using a c</span>omma-separated values table as a source, all necessary files and lines of codes are automatically create for all the provinces and baronies in the source file.</p><p align=\"justify\">This is a super leightweight little tool I wrote for myself. It\'s not fancy, but it get\'s the job done with incredible efficiency.</p><p align=\"justify\">GitHub Repo: </p><p align=\"justify\"><a href=\"https://github.com/Araxiel/CK2-Province_Set-Upper\"><span style=\" font-size:7pt; text-decoration: underline; color:#0000ff;\">https://github.com/Araxiel/CK2-Province_Set-Upper</span></a></p><p align=\"justify\">Written by:</p><p align=\"justify\"><span style=\" font-weight:600;\">Araxiel</span></p></body></html>"))
        self.pushButton_exit.setText(_translate("AboutUI", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutUI = QtWidgets.QDialog()
    ui = Ui_AboutUI()
    ui.setupUi(AboutUI)
    AboutUI.show()
    sys.exit(app.exec_())

