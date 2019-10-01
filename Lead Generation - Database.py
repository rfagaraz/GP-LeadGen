print ("Importing Modules")
import pandas as pd
import numpy as np
import glob
import re
from openpyxl import load_workbook



print("Analyzing files...")
all_data = pd.DataFrame()
for files in glob.glob('C:\\Users\\rfagaraz\\Documents\\Geração de Bases p. Telemarketing\\Extrações do HUBSPOT\\2019-09-23\\*.xlsx'):
   df = pd.read_excel(files)
   all_data = all_data.append(df, ignore_index=False)   
print("All files have been concatenated. Accessing folder...")

book = load_workbook('C:\\Users\\rfagaraz\\Documents\\Geração de Bases p. Telemarketing\\Template.xlsx')
writer = pd.ExcelWriter('C:\\Users\\rfagaraz\\Documents\\Geração de Bases p. Telemarketing\\Template.xlsx', engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
print("Running Regex")

all_data.replace(to_replace ="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_)?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\))(\s|-|\.|\+|\_){0,2}?((?!9999)\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", value=r"\4-\6\8", regex=True, inplace=True)
print("Regex sucessfully applied. Excluding unmatched results")

all_data.filter(regex="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_)?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\))(\s|-|\.|\+|\_){0,2}?(\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", axis=1)
all_data=all_data.drop(all_data[all_data['Phone Mask'].map(len) < 11].index)
print("Successfully filtered results. Saving file...")

all_data.to_excel(writer, sheet_name='Base Original')
writer.save()
print ("Done")
