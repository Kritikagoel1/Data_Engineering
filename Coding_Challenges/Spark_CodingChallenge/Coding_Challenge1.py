#!/usr/bin/env python
# coding: utf-8
#groupby with aggeragte functions
# In[5]:


from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("test").getOrCreate()
newdf=spark.read.csv("C:\\Users\\hp\\OneDrive\\Desktop\\EmployeeDetails.csv",header=True, inferSchema=True)
newdf.show()


# In[6]:


newdf.groupBy("name").sum("salary").show()


# In[8]:


newdf.groupBy("name").count().show()


# In[10]:


newdf.groupBy("name").avg("salary").show()


# In[13]:


newdf.groupBy("name").min("year_joined").show()


# In[14]:


newdf.groupBy("name").max("year_joined").show()


# In[15]:


newdf.groupBy("name").mean("salary").show()


# In[16]:


newdf.groupBy("name").agg(({"salary":"sum"})).show()


#dropping in pyspark
# In[21]:


#drops all the null values
newdf.na.drop().show()



# In[22]:


newdf.na.drop(how="all").show()


# In[25]:


newdf.na.drop(how="any",thresh=2).show() 


# In[32]:


newdf.na.drop(how="any",subset=["gender"]).show()


#sorting
# In[31]:


newdf.sort("salary").show() 


# In[36]:


newdf.sort(newdf["salary"].desc()).show() 


# In[37]:


newdf.sort("salary","year_joined").show() # Sort based on first column then second column


#order by
# In[38]:


newdf.orderBy("salary").show() 







