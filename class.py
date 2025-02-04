import pandas as pd
import matplotlib.pyplot as plt
quarter={
    'month':['jan', 'feb', 'march'],
    'sales':[50, 60, 80],
    'profit':[200, 250, 300],
    'exp':[500, 200, 350]
}
df=pd.DataFrame(quarter)
print(df)

x=df['sales']
y=df['month']
plt.bar(y, x)
plt.show()