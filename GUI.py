# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CORREDOR.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


#!python 3

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter.ttk import *
import pandas as pd #Main Analysis 
import numpy as np #Complementary 
import glob #Excel Reader
import re #Regex
import time #Fancy shit
from openpyxl import load_workbook                                
from os import path

all_data = pd.DataFrame()     #We're gonna use a Dataframe to mess with the docs. 

hubspotDirectory = filedialog.askdirectory()

def appender(hubfolder, data):
       for files in glob.glob(hubfolder+'/*.xlsx'):            #Loop for every hubspot list in the same directory as the script
              appealCampaign = re.search("(?!extracao-)\w+(?=-novos)", files)      #Regex to pull name of the list as "Appeal"
              df = pd.read_excel(files).assign(Appeal=appealCampaign.group())
              data = data.append(df, ignore_index=False)
       return data

appender(hubspotDirectory, all_data)

#TODO: Point the template directory using an integrated User Interface
templateBook = filedialog.askopenfilename(filetypes = (("Excel file", "*.xlsx"), ("all files", "*.*")))
book = load_workbook(templateBook)
writer = pd.ExcelWriter(templateBook, engine='openpyxl') #This path leads to the template file where the dataframe should be pasted
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

def regex(x):
       print('iniciando correções')
       x.replace(to_replace ="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_)?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\))(\s|-|\.|\+|\_){0,2}?((?!9999)\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", value=r"\4-\6\8", regex=True, inplace=True)
       x.filter(regex="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_)?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\))(\s|-|\.|\+|\_){0,2}?(\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", axis=1)
       print('correções finalizadas!')
       return x

def dropRegex(x):
       print("droppando")
       x = x.drop(x[x['Phone Mask'].map(len) < 11 ].index)
       print("finalizado")
       return x


def saveFile (x):
       print('Salvando...')
       x = x.to_excel(writer, sheet_name='Base Original') #Excel folder which it'll be pasted on
       writer.save()
       return x
       print('Finalizado')




class Ui_Dialog(object):

    def helloworld(self):
        self.textBrowser.append("Hello, world")

    def run():
        saveFile(dropRegex(regex(appender(hubspotDirectory, all_data))))

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
        self.pushButton_Hub.clicked.connect(self.run)
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
