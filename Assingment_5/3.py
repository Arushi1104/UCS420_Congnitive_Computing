# Q3
import numpy as np

# a
X = 140
sales = np.array([X, X+50, X+100, X+150, X+200])
print(sales)

# b
tax_rate = ((X % 5) + 5) / 100
print(tax_rate)

tax_applied_sales = sales * (1 + tax_rate)
print(tax_applied_sales)

#c
print(X+100)
discounted_sales = np.where(sales < X+100, sales * 0.95, sales * 0.90)
print(discounted_sales)

#d
sales_matrix = np.tile(sales, (3, 1))
print(sales_matrix)

weeks = np.arange(3).reshape(3, 1)
sales_increase = sales_matrix * (1 + 0.02 * weeks)
print(sales_increase)
