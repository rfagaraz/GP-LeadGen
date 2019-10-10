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

#hubspotDirectory = filedialog.askdirectory()

def appender(data):
       
       for files in glob.glob(filedialog.askdirectory()+'/*.xlsx'):                                #Loop for every hubspot list in the same directory as the script
              appealCampaign = re.search("(?!extracao-)\w+(?=-novos)", files)      #Regex to pull name of the list as "Appeal"
              df = pd.read_excel(files).assign(Appeal=appealCampaign.group())
              data = data.append(df, ignore_index=False)
       return data

#appender(hubspotDirectory, all_data)

templateBook = filedialog.askopenfilename(filetypes = (("Excel file", "*.xlsx"), ("all files", "*.*")))
book = load_workbook(templateBook)
writer = pd.ExcelWriter(templateBook, engine='openpyxl')                                                 #This path leads to the template file where the dataframe should be pasted
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

def run():
       run = saveFile(dropRegex(regex(appender(all_data))))
       run


######################### - USER INTERFACE  - ##########################

window = Tk()
window.title("GUI Project")
window.geometry('525x300')
btn = Button(window, text="RUN", command=run)
btn.grid(column=2, row=0)


window.mainloop()

########################################################################