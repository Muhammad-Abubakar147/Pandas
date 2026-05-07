import pandas as pd

data ={
    "Name":["Abubakar","Ammar","Hamza"],
    "Age":[21,19,19],
    "City":["Fiaslabad","Samnabad","Nvolty pull"],
}
df=pd.DataFrame(data)
print(df)

df.to_csv("output.csv",index=False)  #This is method to save data =>in csv file 
df.to_excel("output.xlsx",index=False) #This is saving in excel form 