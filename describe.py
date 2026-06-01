import pandas as pd 

df=pd.read_csv("Job_Placement_Data.csv")

print(df) #It will show all data in job placement csv file

print("Job Placement Data Describe")

print(df.describe()) #It will describe all about data in job placement
