# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CORREDOR.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets





class Ui_Dialog(object):

    def helloworld(self):
        self.textBrowser.append("Hello, world")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(279, 360)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Hub = QtWidgets.QPushButton(Dialog)
        self.pushButton_Hub.setObjectName("pushButton_Hub")
        self.gridLayout.addWidget(self.pushButton_Hub, 0, 0, 1, 1)
        self.pushButton_Templ = QtWidgets.QPushButton(Dialog)
        self.pushButton_Templ.setEnabled(False)
        self.pushButton_Templ.setObjectName("pushButton_Templ")
        self.gridLayout.addWidget(self.pushButton_Templ, 1, 0, 1, 1)
        self.pushButton_Run = QtWidgets.QPushButton(Dialog)
        self.pushButton_Run.setEnabled(False)
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.gridLayout.addWidget(self.pushButton_Run, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)
        self.actionTest = QtWidgets.QAction(Dialog)
        self.actionTest.setCheckable(False)
        self.actionTest.setObjectName("actionTest")

        self.retranslateUi(Dialog)
        self.pushButton_Hub.clicked.connect(self.helloworld)
        self.pushButton_Hub.clicked.connect(self.helloworld)
        self.pushButton_Templ.clicked.connect(self.pushButton_Run.toggle)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Hub.setText(_translate("Dialog", "Print fucking 'hello, world'"))
        self.pushButton_Templ.setText(_translate("Dialog", "Template File"))
        self.pushButton_Run.setText(_translate("Dialog", "Run"))
        self.actionTest.setText(_translate("Dialog", "Test"))
        self.actionTest.setWhatsThis(_translate("Dialog", "<html><head/><body><p>This is a test action</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
