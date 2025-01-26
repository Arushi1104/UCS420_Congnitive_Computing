#Q4 
import pandas as pd
irisdf= pd.read_csv("iris.csv")
print(irisdf.head(5))

# Q5
df1= irisdf.drop(index=4).drop(irisdf.columns[3], axis=1)
print(df1)
