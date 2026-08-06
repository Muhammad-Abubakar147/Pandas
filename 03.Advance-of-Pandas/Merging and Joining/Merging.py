#merge() combines DataFrames based on one or more common columns, similar to SQL JOIN.

#syntax => pd.merge(left_df, right_df, on="column_name", how="join_type")

import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Ahmed"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [85, 90, 78]
})

result = pd.merge(students, marks, on="ID")
print(result)