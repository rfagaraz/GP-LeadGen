#!python3
import glob
import re
import pandas as pd 
from tkinter import filedialog

def appender(data):
    for files in glob.glob(filedialog.askdirectory()+'/*.xlsx'):                                
           appealCampaign = re.search("(?!extracao-)\w+(?=-novos)", files)      
           df = pd.read_excel(files).assign(Appeal=appealCampaign.group())
           data = data.append(df, ignore_index=False)
    return data
    
