import pandas as pd
import matplotlib.pyplot as plt
quarter={
    # 'month':['jan', 'feb', 'march'],
    'id':[101, 102, 103, 104,105],
    'sales':[500, 600, 700, 800, 900],

}

df=pd.DataFrame(quarter)

profit=0
sales=0
for i in range(5):
    profit=profit+0.8*df['sales']
    sales=sales+df['sales']


print("profit", profit)
print("sales", sales/5)
# df=pd.DataFrame(quarter)
# print(df)

max=0
id=0
for i in range(5):
    if max<df['sales'][i]:
        max=df['sales'][i]
        id=df['id'][i]

print("max and by", max, id)

x=df['sales']
y=df['id']
plt.pie(x)
plt.show()