import pandas as pd

#Q6

employee_data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice ', 'Bob ', 'Charlie', 'Diana', 'Edward'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
    'Age': [29, 34, 41, 28, 38],
    'Salary': [50000, 70000, 65000, 55000, 60000],
    'Years_of_Experience': [4, 8, 10, 3, 12],
    'Joining_Date': ['2020-03-15', '2017-07-19', '2013-06-01', '2021-02-10', '2010-11-25'],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'Bonus': [5000, 7000, 6000, 4500, 5000],
    'Rating': [4.5, 4.0, 3.8, 4.7, 3.5]
}
employees_df = pd.DataFrame(employee_data)
employees_df.to_csv('employees.csv', index=False)

# a) 
print(employees_df.shape)

# b) 
print(employees_df.info())

# c) 
print(employees_df.describe())

# d)
print(employees_df.head(5))
print(employees_df.tail(3))

# e)
print(employees_df['Salary'].mean())
print(employees_df['Bonus'].sum())
print(employees_df['Age'].min())
print(employees_df['Rating'].max())

# f) 
SortedDf = employees_df.sort_values(by='Salary', ascending=False)
print(SortedDf)

# g)
def categorize_rating(rating):
    if rating >= 4.5:
        return 'Excellent'
    elif rating >= 4.0:
        return 'Good'
    else:
        return 'Average'

employees_df['PerformanceRating'] = employees_df['Rating'].apply(categorize_rating)
print(employees_df)

# h) 
print( employees_df.isnull().sum())

# i)
employees_df.rename(columns={'Employee_ID': 'ID'}, inplace=True)
print(employees_df)

# j) 
experienced= employees_df[employees_df['Years_of_Experience'] > 5]
IT_employees = employees_df[employees_df['Department'] == 'IT']
print(experienced)
print(IT_employees)

# k) 
employees_df['Tax'] = employees_df['Salary'] * 0.1
print(employees_df)

# l)
employees_df.to_csv("modified_employees.csv", index=False)