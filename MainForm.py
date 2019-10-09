# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chainsaw(object):
    def setupUi(self, Chainsaw):
        Chainsaw.setObjectName("Chainsaw")
        Chainsaw.resize(482, 348)
        Chainsaw.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Chainsaw)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 451, 301))
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 70, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(156, 32, 281, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 311, 31))
        self.label_2.setObjectName("label_2")
        Chainsaw.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Chainsaw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 21))
        self.menubar.setObjectName("menubar")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        Chainsaw.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Chainsaw)
        self.statusbar.setObjectName("statusbar")
        Chainsaw.setStatusBar(self.statusbar)
        self.actionFuncoes = QtWidgets.QAction(Chainsaw)
        self.actionFuncoes.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionFuncoes.setObjectName("actionFuncoes")
        self.actionContato = QtWidgets.QAction(Chainsaw)
        self.actionContato.setObjectName("actionContato")
        self.menuSobre.addAction(self.actionFuncoes)
        self.menuSobre.addAction(self.actionContato)
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(Chainsaw)
        QtCore.QMetaObject.connectSlotsByName(Chainsaw)

    def retranslateUi(self, Chainsaw):
        _translate = QtCore.QCoreApplication.translate
        Chainsaw.setWindowTitle(_translate("Chainsaw", "MainWindow"))
        self.groupBox.setTitle(_translate("Chainsaw", "Soluções DataBase GPBR"))
        self.pushButton.setText(_translate("Chainsaw", "Concatenator"))
        self.pushButton_2.setText(_translate("Chainsaw", "Telefone REGEX"))
        self.label.setText(_translate("Chainsaw", "Agrupamento de arquivos excel para gerar Leads"))
        self.label_2.setText(_translate("Chainsaw", "  Validação e correção de telefones para  excel"))
        self.menuSobre.setTitle(_translate("Chainsaw", "Sobre"))
        self.actionFuncoes.setText(_translate("Chainsaw", "Funções"))
        self.actionContato.setText(_translate("Chainsaw", "Contato"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Chainsaw = QtWidgets.QMainWindow()
    ui = Ui_Chainsaw()
    ui.setupUi(Chainsaw)
    Chainsaw.show()
    sys.exit(app.exec_())
