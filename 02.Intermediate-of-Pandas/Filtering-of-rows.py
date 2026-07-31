import pandas as pd 


data ={
    "Name":["Abubakar","Ammar","Hamza","Moiz Ahmad","Zubair","Faizan","Fahad"],
    "Age":[21,19,19,23,24,25,26],
    "City":["Fiaslabad","Samnabad","Nvolty pull","Samanabad","Samanabad","Samanabad","Samanabad"],
    "Salary":[20000,30000,40000,50000,60000,70000,350000]
}

df=pd.DataFrame(data)

# print(df)

#how to filter a single row in pandas

print("Displaying employees whos salay is > than 30000")
high_salary= df[df["Salary"]>30000]

print(high_salary)

#How to Filter multiple rows in pandas 

print("Displaying employees whos salary > 30000 & age > 20")

filtered=df[(df["Salary"]>4000) & (df["Age"]>25)]

print(filtered)