import pandas as pd

df = pd.DataFrame({
    "Marks": [80, None, None, 90, 95]
})

print("Original DataFrame:")
print(df)

df["Marks"] = df["Marks"].bfill()

print("\nAfter bfill():") #bfill stands for backword fill method 
print(df)


#output
# Original DataFrame:
#    Marks
# 0   80.0
# 1    NaN
# 2    NaN
# 3   90.0
# 4   95.0

# After bfill():
#    Marks
# 0   80.0
# 1   90.0
# 2   90.0
# 3   90.0
# 4   95.0