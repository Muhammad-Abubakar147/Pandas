#Missing data is very basic concept in pandas and how can we handle it in pandas we will disscuss here .Pandas give us some methods which is use in handling missing data .

import pandas as pd 

data ={
    "Name":["Abubakar","Ammar","Hamza","Moiz Ahmad","Zubair","Faizan","Fahad"],
    "Age":[21,19,19,23,24,25,26],
    "City":["Fiaslabad","Samnabad","Nvolty pull","Samanabad","Samanabad","Samanabad","Samanabad"],
    "Salary":[20000,30000,40000,50000,60000,70000,350000]
}

df=pd.DataFrame(data)

#syntax for detect missing data in data 
print(df.isnull()) #will print(falseif data is not missing)