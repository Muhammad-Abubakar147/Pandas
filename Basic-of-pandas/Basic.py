#Students Class Data
import pandas as pd

DATA = {
    "NAME": ["muhammad", "abubakar" , "ammar"],
    "age": [21, 32 ,32],
    "city": ["faisalabad", "samnabad"  ,"lahore"]
}

df = pd.DataFrame(DATA)
print(df)