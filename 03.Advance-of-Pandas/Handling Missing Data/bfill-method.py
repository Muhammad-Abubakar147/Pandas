import pandas as pd

df = pd.DataFrame({
    "Marks": [80, None, None, 90, 95]
})

print("Original DataFrame:")
print(df)

df["Marks"] = df["Marks"].bfill()

print("\nAfter bfill():") #bfill stands for backword fill method 
print(df)