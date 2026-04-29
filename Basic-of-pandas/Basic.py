#Students Class Data
import pandas as pd

DATA = {
    "NAME": ["muhammad", "abubakar"],
    "age": [21, 32],
    "city": ["faisalabad", "samnabad"]
}

df = pd.DataFrame(DATA)
print(df)