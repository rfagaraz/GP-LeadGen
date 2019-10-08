#python3
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
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

#hubspotExtractionDirectory = filedialog.askdirectory()

def CONCATENATOR(hubspotExtractionDirectory):
   for files in glob.glob(hubspotExtractionDirectory+'/*.xlsx'):            #Loop for every hubspot list in the same directory as the script
       appealCampaign = re.search("(?!extracao-)\w+(?=-novos)", files)      #Regex to pull name of the list as "Appeal"
       time.sleep(1)
       df = pd.read_excel(files).assign(Appeal=appealCampaign.group())
       #all_data = all_data.append(df, ignore_index=False)              #Concatenate all files in the loop