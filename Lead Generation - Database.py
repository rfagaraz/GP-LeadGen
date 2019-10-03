from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter.ttk import *


#Create an Interface:
window = Tk()
window.title("GUI Project")
window.geometry('720x500')
txt = scrolledtext.ScrolledText(window,width=100,height=100)
txt.grid(column=0, row=0)

txt.insert(INSERT, "Importing Modules\n")

import pandas as pd #Main Analysis 
import numpy as np #Complementary 
import glob #Excel Reader
import re #Regex
import time #Fancy shit
from openpyxl import load_workbook                                
from os import path

txt.insert(INSERT, "The following Appeals have been treated:\n")
time.sleep(4)
all_data = pd.DataFrame()     #We're gonna use a Dataframe to mess with the docs. 
messagebox.showinfo('Warning', 'Please select the folder containing all Hubspot files extracted')
hubspotExtractionDirectory = filedialog.askdirectory()

for files in glob.glob(hubspotExtractionDirectory+'/*.xlsx'):            #Loop for every hubspot list in the same directory as the script
   appealCampaign = re.search("(?!extracao-)\w+(?=-novos)", files)      #Regex to pull name of the list as "Appeal"
   txt.insert(INSERT,(appealCampaign.group())+'\n')
   time.sleep(1)
   df = pd.read_excel(files).assign(Appeal=appealCampaign.group())
   all_data = all_data.append(df, ignore_index=False)              #Concatenate all files in the loop
   txt.insert(INSERT, "All files have been concatenated. Accessing template sheet...\n")

time.sleep(10)
#TODO: Point the template directory using an integrated User Interface
messagebox.showinfo('Warning',"Please select your Template file")
templateBook = filedialog.askopenfilenames(filetypes = (("xlsx files", "*.xlsx"), ("all files", "*.*")))
book = load_workbook(templateBook)
writer = pd.ExcelWriter(templateBook, engine='openpyxl') #This path leads to the template file where the dataframe should be pasted
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

txt.insert(INSERT, "Running regex to clean Phone Numbers...\n") #It's currently a messy REGEX, but it delivers the number structure required by the TLMKT agency
time.sleep(1)
all_data.replace(to_replace ="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_)?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\))(\s|-|\.|\+|\_){0,2}?((?!9999)\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", value=r"\4-\6\8", regex=True, inplace=True)
txt.insert(INSERT, "Phone Numbers cleaned. Excluding unmtched entries...\n")
time.sleep(1)
all_data.filter(regex="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_)?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\))(\s|-|\.|\+|\_){0,2}?(\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", axis=1)
all_data=all_data.drop(all_data[all_data['Phone Mask'].map(len) < 11].index)
txt.insert(INSERT, "Successfully filtered results. Saving file...\n")

all_data.to_excel(writer, sheet_name='Base Original') #Excel folder which it'll be pasted on
writer.save()
txt.insert(INSERT, "Done!\n")
time.sleep(3)
