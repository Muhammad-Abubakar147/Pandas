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