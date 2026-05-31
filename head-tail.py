import pandas as pd

df=pd.read_csv("Job_Placement_Data.csv")
print("First five rows of data")

print(df.head()) #This is for reading first 5 rows 

#This is for reading end 5 rows
print("Last five rows of data")

print(df.tail())

#If uh want to read specific rows of data thsn use this

print("This is specific rows")

print(df.tail(17)) 