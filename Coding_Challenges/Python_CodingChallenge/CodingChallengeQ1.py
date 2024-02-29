import pandas as pd
data = pd.read_csv("Employees.csv")
var=data.Salary
print(var)

import pandas as pd
df = pd.read_csv('Employees.csv')
print(df.head())#reading the top 5 rows of csv file

import pandas as pd
df = pd.read_csv('Employees.csv')
print(df.describe())


import pandas as pd
df = pd.read_csv('employees.csv')
filtered_df = df.query('Salary > 1800000 and Name == "Joy"')
print(filtered_df)

import pandas as pd
df = pd.read_csv('employees.csv')
average_salary = df['Salary'].mean()
print("\nAverage Salary:", average_salary)

