
# coding: utf-8

# In[10]:

# Merge, join, and concatenate
# http://pandas.pydata.org/pandas-docs/stable/merging.html

# Modify individual cells?

# Write to files
# http://pandas.pydata.org/pandas-docs/stable/io.html

import pandas
import os
os.listdir()


# In[22]:

df1=pandas.read_json('supermarkets.json')
df2=pandas.read_csv('supermarkets_semi-colons.txt', sep=None, engine='python')


# In[33]:

# Concatenating
df3=pandas.concat([df1, df2])
df3.set_index('ID')


# In[35]:

# writing
df3.to_html('test_file.html')


# In[41]:

# check that we can read it
df4=pandas.read_html('test_file.html')
df4

