import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('company_sales_data.csv')

# Read Total profit of all months
total_profit = data['total_profit']

# Plot using a line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x=data['month_number'], y=total_profit, marker='o', color='blue')
plt.title('Total Profit of All Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid(True)
plt.show()

# Read Total profit of all months
total_profit = data['total_profit']

# Plot using a line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x=data['month_number'], y=total_profit, marker='o', color='blue')
plt.title('Total Profit of All Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid(True)
plt.show()

# Plot using a bar chart for all features/attributes
data.set_index('month_number').plot(kind='bar', figsize=(15, 10))
plt.title('Bar Chart of All Features/Attributes')
plt.xlabel('Month')
plt.ylabel('Values')
plt.grid(True)
plt.legend(title='Features')
plt.show()
