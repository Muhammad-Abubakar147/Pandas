#here we will disscus how to filter a single column and multiple columns in pandas ..

import pandas as pd 


data ={
    "Name":["Abubakar","Ammar","Hamza","Moiz Ahmad","Zubair","Faizan","Fahad"],
    "Age":[21,19,19,23,24,25,26],
    "City":["Fiaslabad","Samnabad","Nvolty pull","Samanabad","Samanabad","Samanabad","Samanabad"],
    "Salary":[20000,30000,40000,50000,60000,70000,350000]
}

df=pd.DataFrame(data)

print(df)