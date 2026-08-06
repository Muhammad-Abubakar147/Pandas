#Agreegassion in pandas is used for the calculate summary for example : mean,sum,and many others .



import pandas as pd 


data ={
    "Name":["Omer","zabiullah","Hassan"],
    "Age":[28,48,59],
    "Salary":[28500,56778,64779]
}

df=pd.DataFrame(data)

print("Average Salary :")
average_slary=df["Salary"].mean()
print(average_slary)