#!python3
import pandas as pd 
from tkinter import filedialog

def excelAccess():
       templateBook = filedialog.askopenfilename(filetypes = (("Excel file", "*.xlsx"), ("all files", "*.*")))
       global writer 
       writer = pd.ExcelWriter(templateBook, engine='openpyxl')
       return writer