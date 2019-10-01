print ("Importing Modules")
import pandas as pd #Main Analysis 
import numpy as np #Complementary 
import glob #Excel Reader
import re #Regex
import time #Fancy shit
from openpyxl import load_workbook


print("The following Appeals have been treated:")
all_data = pd.DataFrame()     #We're gonna use a Dataframe to mess with the docs. 


for files in glob.glob('*.xlsx'):            #Loop for every hubspot list in the same directory as the script
   appealCampaign = re.search("(?!extracao-)\w+(?=-novos)", files)      #Regex to pull name of the list as "Appeal"
   print(appealCampaign.group())
   time.sleep(1)
   df = pd.read_excel(files).assign(Appeal=appealCampaign.group())
   all_data = all_data.append(df, ignore_index=False)              #Concatenate all files in the loop
print("All files have been concatenated. Accessing template sheet...")

time.sleep(1)
#TODO: Point the template directory using an integrated User Interface
book = load_workbook('C:\\Users\\rfagaraz\\Documents\\Geração de Bases p. Telemarketing\\Template.xlsx')
writer = pd.ExcelWriter('C:\\Users\\rfagaraz\\Documents\\Geração de Bases p. Telemarketing\\Template.xlsx', engine='openpyxl') #This path leads to the template file where the dataframe should be pasted
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

print("Running regex to clean Phone Numbers...") #It's currently a messy REGEX, but it delivers the number structure required by the TLMKT agency
time.sleep(1)
all_data.replace(to_replace ="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_)?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\))(\s|-|\.|\+|\_){0,2}?((?!9999)\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", value=r"\4-\6\8", regex=True, inplace=True)
print("Phone Numbers cleaned. Excluding unmtched entries...")
time.sleep(1)
all_data.filter(regex="^(\+55|55|055|\s\+55|\s55|\s055){0,1}?(\s|-|\.|\+|\_)?(0{0,1}\s{0,1})?([1-9][0-9]|\([1-9][0-9]\))(\s|-|\.|\+|\_){0,2}?(\d{4,5}){0,1}?(\s|-|\.|\+|\_)?((?!0000)\d{4,5})$", axis=1)
all_data=all_data.drop(all_data[all_data['Phone Mask'].map(len) < 11].index)
print("Successfully filtered results. Saving file...")

all_data.to_excel(writer, sheet_name='Base Original') #Excel folder which it'll be pasted on
writer.save()
print ("Done!")
time.sleep(3)
