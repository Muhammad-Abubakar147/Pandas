#How ro make data frame

import pandas as pd

data ={
    "Name":["Abubakar","Ammar","Hamza"],
    "Age":[21,19,19],
    "City":["Fiaslabad","Samnabad","Nvolty pull"],
}

df=pd.DataFrame(data)
print(df)
