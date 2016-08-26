
# coding: utf-8

# In[1]:

import pandas


# In[20]:

df1=pandas.read_json('supermarkets.json')
df1=df1.set_index('Address')


# In[21]:

# 1 to indicate you are deleting a column
df1.drop("ID", 1)


# In[22]:

# 0 to indicate you are deleting a row
df1.drop("3995 23rd St", 0)


# In[26]:

# To delete by index, need to use a few tricks
#  we use either .columns or .index method to call by index, which will in call the approptiate label
df1.index


# In[41]:

# deletes rows by default
df1.drop(df1.index[0:2])


# In[34]:

df1.columns


# In[39]:

df1.drop(df1.columns[0:1],1)

