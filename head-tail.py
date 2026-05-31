import pandas as pd

df=pd.read_csv("Job_Placement_Data.csv")
print("First five rows of data")
print(df.head()) #This is for reading first 5 rows 

#This is for reading end 5 rows
print("Last five rows of data")

print(df.tail())