#how to handle missing data in pandas ,How to drop those data which is missing in data and not essential for us .


import pandas as pd 

data ={
    "Name":["Abubakar",None,"Hamza","Moiz Ahmad","Zubair","Faizan","Fahad"],
    "Age":[21,None,19,23,24,25,26],
    "City":["Fiaslabad",None,"Nvolty pull","Samanabad","Samanabad","Samanabad","Samanabad"],
    "Salary":[20000,None,40000,50000,60000,70000,350000]
}

df=pd.DataFrame(data)

#How tp drop missing data 

df.dropna(inplace=True)
print(df)


#if we pass this syntax 
# df.dropna(axis=0,inplace=True) axis=0 work for rows removing from the data 
#df.dropna(axis=1,inplace=True)  axis=0 work for columns removing from the data .