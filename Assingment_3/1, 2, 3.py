#Q1
import pandas as pd
data={
    'Tid' : [1,2,3,4,5,6,7,8,9,10],
    'Refund' : ['Yes','No','No','Yes','No','No','Yes','No','No','No'],
    'Marital Status' : ['Single','Married','Single','Married','Divorced','Married','Divorced','Single','Married','Single'],
    'Taxable Income' : ['125K','100K','70K','120K','95K','60K','220K','85K','75K','90K'],
    'Cheat' : ['No','No','No','No','Yes','No','No','Yes','No','Yes']}
df=pd.DataFrame(data)
print(df)

#Q2
Row=df.loc[[0,4,7,8]]
print(Row)

#Q3
a=df.iloc[3:8]
print(a)
b=df.iloc[4:9,2:5]
print(b)
c=df.iloc[:,1:4]
print(c)

# #Q4 Read a csv file and display its first five rows. 
# irisdf= pd.read_csv("iris.csv")
# print(irisdf.head(5))

# # Q5: Delete row 4 and column 3 from the CSV file
# df1= irisdf.drop(index=4).drop(irisdf.columns[3], axis=1)
# print(df1)

# # Q6: Create a sample dataset (employees.csv) and perform tasks
# employee_data = {
#     'Employee_ID': [101, 102, 103, 104, 105],
#     'Name': ['Alice ', 'Bob ', 'Charlie', 'Diana', 'Edward'],
#     'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
#     'Age': [29, 34, 41, 28, 38],
#     'Salary': [50000, 70000, 65000, 55000, 60000],
#     'Years_of_Experience': [4, 8, 10, 3, 12],
#     'Joining_Date': ['2020-03-15', '2017-07-19', '2013-06-01', '2021-02-10', '2010-11-25'],
#     'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
#     'Bonus': [5000, 7000, 6000, 4500, 5000],
#     'Rating': [4.5, 4.0, 3.8, 4.7, 3.5]
# }
# employees_df = pd.DataFrame(employee_data)
# employees_df.to_csv('employees.csv', index=False)

# # a) Shape of the DataFrame
# print(employees_df.shape)

# # b) Summary of the DataFrame
# print(employees_df.info())

# # c) Descriptive statistics
# print(employees_df.describe())

# # d) First 5 rows and last 3 rows
# print(employees_df.head(5))
# print(employees_df.tail(3))

# # e) Calculate the following statistics from the dataset: 
# print(employees_df['Salary'].mean())
# print(employees_df['Bonus'].sum())
# print(employees_df['Age'].min())
# print(employees_df['Rating'].max())

# # f)  Sort the DataFrame by the Salary column in descending order. 
# SortedDf = employees_df.sort_values(by='Salary', ascending=False)
# print(SortedDf)

# # g)Add a new column that categorizes employees based on their performance rating: 
# def categorize_rating(rating):
#     if rating >= 4.5:
#         return 'Excellent'
#     elif rating >= 4.0:
#         return 'Good'
#     else:
#         return 'Average'

# employees_df['PerformanceRating'] = employees_df['Rating'].apply(categorize_rating)
# print(employees_df)

# # h) Identify missing values in the DataFrame. 
# print( employees_df.isnull().sum())

# # i)Rename the Employee_ID column to ID.
# employees_df.rename(columns={'Employee_ID': 'ID'}, inplace=True)
# print(employees_df)

# # j) Find employees with more than 5 years of experience and in IT department
# experienced= employees_df[employees_df['Years_of_Experience'] > 5]
# IT_employees = employees_df[employees_df['Department'] == 'IT']
# print(experienced)
# print(IT_employees)

# # k) Modify the dataset by adding a new column, Tax, which deducts 10% of the Salary
# employees_df['Tax'] = employees_df['Salary'] * 0.1
# print(employees_df)

# # l) Save the modified DataFrame (with added columns) to a new CSV file. 
# employees_df.to_csv("modified_employees.csv", index=False)