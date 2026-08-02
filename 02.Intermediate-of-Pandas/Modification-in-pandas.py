#Here we will disscuss how to modified new things in pandas like how to add new columns how to add rows and how to remove both and many things .


import pandas as pd 

data ={
    "Name":["Abubakar","Ammar","Hamza","Moiz Ahmad","Zubair","Faizan","Fahad"],
    "Age":[21,19,19,23,24,25,26],
    "City":["Fiaslabad","Samnabad","Nvolty pull","Samanabad","Samanabad","Samanabad","Samanabad"],
    "Salary":[20000,30000,40000,50000,60000,70000,350000]
}

df=pd.DataFrame(data)

#first method is assingment method and other is insert method 

#by Assingment method new column will add at end of the data set

df["Bonus"]=df["Salary"]*0.1
print(df) #it will add at the end of the column not at fvrt index 

#for specific index (insert method) is used . 

df.insert(0,"Employee Id",[10,20,30,40,50,60,70])

print(df)