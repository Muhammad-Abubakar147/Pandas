#This will tell how much ur data is big ..
#Tell the numbers of columns and rows in ur data set .. 
#Tell the name of ur columns ..

import pandas as pd 

data =pd.read_csv("Job_Placement_Data.csv")
print("Data is dipalying :")
print(data)

print(f"shape : {data.shape}") #It will print shape of data means that how much rows and cloumns 

print(f"Columns :{data.columns}") #it will print names of columns in data .