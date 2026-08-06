#groupby() in Pandas is used to group rows that have the same value in one or more columns and then perform calculations on each group separately.

import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Salary": [50000, 40000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].mean()
print(result)

# Department
# HR       42500.0
# IT       55000.0
# Sales    55000.0
# Name: Salary, dtype: float64


df.groupby("Department")["Salary"].sum()      # Total salary
df.groupby("Department")["Salary"].mean()     # Average salary
df.groupby("Department")["Salary"].max()      # Maximum salary
df.groupby("Department")["Salary"].min()      # Minimum salary
df.groupby("Department")["Salary"].count()    # Number of employees

print("ALL ABOUT GROUPING OF DATA :")
print(df)


# ALL ABOUT GROUPING OF DATA :
#   Department  Salary
# 0         IT   50000
# 1         HR   40000
# 2         IT   60000
# 3         HR   45000
# 4      Sales   55000 (output)