#Missing data is very basic concept in pandas and how can we handle it in pandas we will disscuss here .Pandas give us some methods which is use in handling missing data .

import pandas as pd 

data ={
    "Name":["Abubakar",None,"Hamza","Moiz Ahmad","Zubair","Faizan","Fahad"],
    "Age":[21,None,19,23,24,25,26],
    "City":["Fiaslabad",None,"Nvolty pull","Samanabad","Samanabad","Samanabad","Samanabad"],
    "Salary":[20000,None,40000,50000,60000,70000,350000]
}

df=pd.DataFrame(data)
print("It will print False in output")
#syntax for detect missing data in data 
print(df.isnull()) #will print(falseif data is not missing) and print(true) if data is missing .
print("It will print All about data that how much data is missing")
#And if uh want to detect how much data is missed in dataset then this method is used for it .
print(df.isnull().sum())



print("this will output on terminal")
# It will print False in output
#     Name    Age   City  Salary
# 0  False  False  False   False
# 1   True   True   True    True
# 2  False  False  False   False
# 3  False  False  False   False
# 4  False  False  False   False
# 5  False  False  False   False
# 6  False  False  False   False
# It will print All about data that how much data is missing
# Name      1
# Age       1
# City      1
# Salary    1
# dtype: int64