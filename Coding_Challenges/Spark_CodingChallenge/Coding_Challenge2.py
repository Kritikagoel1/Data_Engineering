#!/usr/bin/env python
# coding: utf-8

# In[5]:
#Joins

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("local").getOrCreate()
DF1 = spark.read.csv("C:\\Users\\hp\\OneDrive\\Desktop\\EmployeeDetails.csv",header=True, inferSchema=True)
DF2=spark.read.csv("C:\\Users\\hp\\OneDrive\\Desktop\\Dept_details.csv",header=True, inferSchema=True)
DF1.show()
DF2.show()


# In[6]:


DF1.join(DF2,DF1.emp_dept_id ==  DF2.dept_id,"inner") .show()


# In[7]:


DF1.join(DF2,DF1.emp_dept_id ==  DF2.dept_id,"outer") .show()


# In[8]:


DF1.join(DF2,DF1.emp_dept_id ==  DF2.dept_id,"right").show()


# In[9]:


DF1.join(DF2,DF1.emp_dept_id ==  DF2.dept_id,"left") .show()


# In[10]:


DF1.join(DF2,DF1.emp_dept_id ==  DF2.dept_id,"leftsemi") .show()


# In[11]:


DF1.join(DF2,DF1.emp_dept_id ==  DF2.dept_id,"leftanti") .show()


#Applyin Functions in Pandas DataFrame
# In[14]:


import pandas as pd
import numpy as np


data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}

df = pd.DataFrame(data)
def square(x):
    return x ** 2
result = df.apply(square)

print(result)


# In[15]:


def column_sum(col):
    return col.sum()
column_sums = df.apply(column_sum, axis=0)
print(column_sums)


# In[16]:


doubled_rows = df.apply(lambda row: row * 2, axis=1)

print(doubled_rows)


# In[ ]:




