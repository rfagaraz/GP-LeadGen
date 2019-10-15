#!python 3
import pandas as pd 
import numpy as np 
from tkinter import *
from tkinter import scrolledtext, messagebox, ttk, filedialog
from tkinter.ttk import Progressbar
from openpyxl import load_workbook 
from src.funAppender import appender
#from src.funExcelAccess import excelAccess
#from src.funAppender import
#from src.funAppender import         

all_data = pd.DataFrame()  
     
def excelAccess():
       templateBook = filedialog.askopenfilename(filetypes = (("Excel file", "*.xlsx"), ("all files", "*.*")))
       global writer 
       book = load_workbook(templateBook)
       writer = pd.ExcelWriter(templateBook, engine='openpyxl')
       writer.book = book
       writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
       return writer

def regex(yourDataFrame):
       print('iniciando correções')
       yourDataFrame.replace(to_replace ="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_){0,2}?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\)){0,1}(\s|-|\.|\+|\_){0,2}?((?!9999)\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", value=r"\4-\6\8", regex=True, inplace=True)
       yourDataFrame.filter(regex="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_){0,2}?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\)){0,1}(\s|-|\.|\+|\_){0,2}?(\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", axis=1)
       print('correções finalizadas!')
       return yourDataFrame

def dropRegex(yourDataFrame, size):
       print("droppando")
       yourDataFrame = yourDataFrame.drop(yourDataFrame[yourDataFrame['Phone Mask'].map(len) < size ].index)
       print("finalizado")
       return yourDataFrame

def saveFile (yourDataFrame):
       print('Salvando...')
       yourDataFrame = yourDataFrame.to_excel(writer, sheet_name='Base Original') #Excel folder which it'll be pasted on
       writer.save()
       return yourDataFrame
       print('Finalizado')

def run():
       run = saveFile(dropRegex(regex(appender(all_data)), 11))
       run
       print('Successfully run!')



######################### - USER INTERFACE  - ##########################

window = Tk()
window.title("GUI Project")
window.geometry('200x100')
runButton = Button(window, text="Execute full script", command=run)
runButton.grid(column=1, row=2)
templateButton = Button(window, text="Select your template", command=excelAccess)
templateButton.grid(column=1, row=1)

window.mainloop()

########################################################################