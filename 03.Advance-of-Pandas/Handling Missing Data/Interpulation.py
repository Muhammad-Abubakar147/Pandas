#Interpulation is a technique which give estimated value for example if our data is 10,20,None,40,50 ,Then this method give us 30 which is estimated value for it .
#There many methods for interpolaton in pandas ike ,linear,polynomial,time etc .

import pandas as pd

df = pd.DataFrame({
    "Marks": [50, 60, None, None, 90]
})

print(df)

df["Marks"]=df["Marks"].interpolate()
print(df)