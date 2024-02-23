'''# with reader
import csv
with open('Employees.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
'
#with pandas
import pandas as pd
data = pd.read_csv("Employees.csv")
var=data.Salary
print(var)


#withDictReader
import csv
with open('Employees.csv','r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)
'''

#with readlines
with open('Employees.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)


