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


#          Name   Age         City    Salary
# 0    Abubakar  21.0    Fiaslabad   20000.0
# 1           0   0.0            0       0.0
# 2       Hamza  19.0  Nvolty pull   40000.0
# 3  Moiz Ahmad  23.0    Samanabad   50000.0
# 4      Zubair  24.0    Samanabad   60000.0
# 5      Faizan  25.0    Samanabad   70000.0
# 6       Fahad  26.0    Samanabad  350000.0