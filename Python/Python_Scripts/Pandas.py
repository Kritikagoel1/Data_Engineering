import pandas as pd

# Read data from a CSV file
df1 = pd.read_csv('EmployeeDetails.csv')
df2 = pd.read_csv('Dept_details.csv')

# inner join
df = pd.merge(df1, df2, on='emp_id')
print(df)

#left join
df = pd.merge(df1, df2, on='emp_id', how='left')
print(df)

#right join
df = pd.merge(df1, df2, on='emp_id', how='right')
print(df)

#outer join
df = pd.merge(df1, df2, on='emp_id', how='outer')
print(df)

# Filtering based on a condition
filtered_df = df1[df1['salary'] > 2000]
print(filtered_df)

# Sorting by a column
sorted_df = df1.sort_values(by='salary', ascending=False)
print(sorted_df)