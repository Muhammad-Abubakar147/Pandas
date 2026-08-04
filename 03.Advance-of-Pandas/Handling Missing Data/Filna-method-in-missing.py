#fillna method use for filling missing data in pandas syntax for it => df.fillna(value,inplace=True)


import pandas as pd 

data ={
    "Name":["Abubakar",None,"Hamza","Moiz Ahmad","Zubair","Faizan","Fahad"],
    "Age":[21,None,19,23,24,25,26],
    "City":["Fiaslabad",None,"Nvolty pull","Samanabad","Samanabad","Samanabad","Samanabad"],
    "Salary":[20000,None,40000,50000,60000,70000,350000]
}

df=pd.DataFrame(data)

#fillna method use for filling missing data 

df.fillna(0,inplace=True)
print(df)