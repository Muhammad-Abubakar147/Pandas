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


#    ID   Name  Marks
# 0   1    Ali     85
# 1   2   Sara     90
# 2   3  Ahmed     78  output


#Types of Data merging :

# df1.join(df2, how="left")
# df1.join(df2, how="right")
# df1.join(df2, how="inner")
# df1.join(df2, how="outer")