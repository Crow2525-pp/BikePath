# BikePath Analysis

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Analysing the effectiveness of Bike Paths in Melbourne
# 
# I'd like to see how effective bike paths are in Melbourne using VicRoads data available from their website.
# 
# Need to import the data

# %%
#import numpy as np
#from  pathlib import Path
#import openpyxl

#Required 
import requests
import pandas as pd
import zipfile, os, re


# %%
#assign variables to vicroads data sources
#header
VicRoadsHeader_URL = 'https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Traffic_Measurement/Bicycle_Volume_and_Speed/VicRoads_Bike_Site_Number_Listing.xlsx'

#Yearly Data
Bicycle_Vol = {'Bicycle_Vol_2021_URL' : 'https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Traffic_Measurement/Bicycle_Volume_and_Speed/Bicycle_Volume_Speed_2021.zip',
               'Bicycle_Vol_2020_URL' : 'https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Traffic_Measurement/Bicycle_Volume_and_Speed/Bicycle_Volume_Speed_2020.zip',
               'Bicycle_Vol_2019_URL' : 'https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Traffic_Measurement/Bicycle_Volume_and_Speed/Bicycle_Volume_Speed_2019.zip',
               'Bicycle_Vol_2018_URL' : 'https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Traffic_Measurement/Bicycle_Volume_and_Speed/Bicycle_Volume_Speed_2018.zip',
               'Bicycle_Vol_2017_URL' : 'https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Traffic_Measurement/Bicycle_Volume_and_Speed/Bicycle_Volume_Speed_2017.zip',
               'Bicycle_Vol_2016_URL' : 'https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Traffic_Measurement/Bicycle_Volume_and_Speed/Bicycle_Volume_Speed_2016.zip',
               'Bicycle_Vol_2015_URL' : 'https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Traffic_Measurement/Bicycle_Volume_and_Speed/Bicycle_Volume_speed_2015.zip'}


# %%
#download header and write it to header excel file
resp = requests.get(VicRoadsHeader_URL)
with open('VicRoadsHeader.xlsx','wb') as output:
        output.write(resp.content)


# %%
df = pd.read_excel('VicRoadsHeader.xlsx')
print(df.head())


# %%
#create an empty list to idenitfy the list zips once created.
Bicycle_Vol_Zip_Files = []

#download zips from website and label using as subset of the dictionary for the URLs  
for key, value in Bicycle_Vol.items():
    resp = requests.get(value)
    with open(key[:-4] + '.zip','wb') as output: #remove the URL part of the key
        output.write(resp.content)
        Bicycle_Vol_Zip_Files.append(key[:-4] + '.zip') #Populate the empty list with filenames.
       


# %%
def extract_nested_zip(zippedFile, toFolder):
       #Unzip a zip file and its contents, including nested zip files
       # Delete the zip file(s) after extraction 
       # Credit - Stackoverflow - ronnydw answered May 10 '17 at 14:47
    
    with zipfile.ZipFile(zippedFile, 'r') as zfile:
        zfile.extractall(path=toFolder)   
    
    os.remove(zippedFile) #Removing the zip once extracted.
    
    #search the dir for zips and send it back to the start of the function.
    for filename in files:
        if re.search(r'\.zip$', filename):
            fileSpec = os.path.join(root, filename)
            extract_nested_zip(fileSpec, root)
    
#        x = zfile.namelist()
#        for i in x:
 #           print(i)
  #          if 'zip' in i:
   #             nestedZippedFile = toFolder[:-1] + i
    #            with zipfile.ZipFile(nestedZippedFile,'r') as zFile2:
     #               print(i)
      #              zFile2.extractall(path=toFolder)
       #         os.remove(nestedZippedFile)
    
    
    #for root, dirs, files in os.walk(toFolder):
     #   for filename in files:
      #      if re.search(r'\.zip$', filename):
       #         fileSpec = os.path.join(root, filename)
        #        extract_nested_zip(fileSpec, root) 


# %%
for File in Bicycle_Vol_Zip_Files:
    extract_nested_zip(File,'zip\.')


# %%
with zipfile.ZipFile('Bicycle_Vol_2021.zip') as z:
    with z.open('Bicycle_Vol_2021.csv') as f:
        DF_2021 = pd.read_csv(f)
        
        print(DF_2021.head())


# %%
'''
xlsx_file = Path(Path.home(),'Projects','Bike Path','text.xlsx')
print(xlsx_file)
wb_obj = openpyxl.load_workbook(xlsx_file)
print(wb_obj)
'''


# %%
'''
sheet = wb_obj.active
for row in sheet.iter_rows(max_row=6):
        for cell in row:
            print(cell.value, end=" ")
        print()
'''


# %%



