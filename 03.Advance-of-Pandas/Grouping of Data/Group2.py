#for grouping of data with multiple column :

import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "IT", "HR"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female"],
    "Salary": [50000, 60000, 40000, 45000, 55000, 47000]
}

df = pd.DataFrame(data)

result = df.groupby(["Department", "Gender"])["Salary"].mean()
print(result)