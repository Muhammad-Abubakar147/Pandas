import pandas as pd 

data ={
    "Name":["Abubakar","Ammar","Hamza","Moiz Ahmad","Zubair","Faizan","Fahad"],
    "Age":[21,19,19,23,24,25,26],
    "City":["Fiaslabad","Samnabad","Nvolty pull","Samanabad","Samanabad","Samanabad","Samanabad"],
    "Salary":[20000,30000,40000,50000,60000,70000,350000]
}

df=pd.DataFrame(data)

#syntax for removing a column 
#df.drop(columns["Column Name"]inplace=True)


print("Removing One column")
df.drop(columns=["City"],inplace=True) #for removing one column

print(df)

print("Removing Multiple column")
df.drop(columns=["City","Age"],inplace=True) #for removing Multiple column

print(df)