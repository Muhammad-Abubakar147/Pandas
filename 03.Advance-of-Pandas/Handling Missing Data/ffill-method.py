import pandas as pd

df = pd.DataFrame({
    "Marks": [80, None, None, 90, 95]
})

print("Original DataFrame:")
print(df)

df["Marks"] = df["Marks"].ffill()

print("\nAfter ffill():")
print(df)


# Original DataFrame:
#    Marks
# 0   80.0
# 1    NaN
# 2    NaN
# 3   90.0
# 4   95.0

# After ffill():
#    Marks
# 0   80.0
# 1   80.0
# 2   80.0
# 3   90.0
# 4   95.0