#Sorting method basically use for the arrang data in meaningfull way . 
#How to sort data .


import pandas as pd 


data ={
    "Name":["Omer","zabiullah","Hassan"],
    "Age":[28,48,59],
    "Salary":[28500,56778,64779]
}

df=pd.DataFrame(data)
print("Orignal Data : ")

print(df)

#For sorting of data syntax is :

df.sort_values(by="Name",ascending=True,inplace=True) #for sorting one column in data 
print("Sorting data :")

print(df)


#Sorting of data for multiple columns 
print("Sorting of data for multiple columns :")

df.sort_values(by=["Name","Age","Salary"],ascending=[True,False,False],inplace=True) #for multiple coulmns

print(df)