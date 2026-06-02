import pandas as pd

DATA = {
    "NAME": ["muhammad", "abubakar" , "ammar"],
    "age": [21, 32 ,32],
    "city": ["faisalabad", "samnabad"  ,"lahore"]
}

df = pd.DataFrame(DATA)
print(df)

print("Structure of data")
print(df.shape ) #It will show all types of data (structure of data)