
# coding: utf-8

# In[3]:

import pandas


# In[95]:

df1=pandas.read_csv('supermarkets.csv')
# df1=df1.set_index('ID') # needs to be set as variable to be persistent
df1.set_index('ID', inplace=True) # this is cool!
df1


# In[113]:

####################################
# Label-based indexing, using ranges or single values (will only accept one value)
df1.loc[2:4, 'Name':'Employees']


# In[126]:

# all entries for one column, ie all indeces for this label
# we can also convert this to list
list(df1.loc[:, 'Address'])


# In[120]:

# One row ie complete line by index
df1.loc[4, :]
#####################


# In[124]:

# Find a specific cell in the dataframe, ie by index and label
df1.loc[3, 'Name']


# In[129]:

####################################
# location-based indexing
# using indeces of rows and columns instead of labels, does the same otherwise
df1


# In[133]:

df1.iloc[:, 4:]


# In[140]:

##### mixed indexing!!!
df1.ix[4,'City':'State']


# In[144]:

df1.ix[4, 1:3]

