
# coding: utf-8

# In[2]:

import os
os.listdir()


# In[3]:

import pandas


# In[21]:

# Excel files may have multiple sheets, specify by index
df1=pandas.read_excel('supermarkets.xlsx', sheetname=1)
df1


# In[15]:

# can ignore header
df2=pandas.read_csv('supermarkets.csv', header=None)
df2


# In[18]:

# Use one of the columns as an index
df2=pandas.read_csv('supermarkets.csv')
df2.set_index('ID')


# In[19]:

# see the shape of the dataframe, ie how many rows and columns there are
df2.shape


# In[26]:

# can specify which delimiter to use for the datastructure
df3=pandas.read_csv('supermarkets_semi-colons.txt', sep=';')
df3


# In[30]:

# can also read file from URL
df4=pandas.read_json('http://pythonhow.com/supermarkets.json')
df4

