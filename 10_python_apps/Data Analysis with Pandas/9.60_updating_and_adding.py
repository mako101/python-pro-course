
# coding: utf-8

# In[150]:

import pandas


# In[151]:

df1=pandas.read_json('supermarkets.json')
df1.set_index('ID', inplace=True)
df1


# In[152]:

#If we want to insert a new column, we need to add value for each row
# We can get the number of rows by using 1st element of the "shape" tuple
rows=df1.shape[0]
rows


# In[153]:

df1['Continent'] = rows * ['North America']
df1


# In[154]:

# A very roundabout way to manipulate the string but works!
# Doesn't like manipulting strings directly
def extract_zipcode():
    zips=[]
    for i in df1.index:
        if (len(df1.loc[i, 'State'].split())) > 1:
            zipcode=df1.loc[i, 'State'].split()[1]
        else:
            zipcode = 'N/A'
        zips.append(zipcode)
    return zips

def get_state():
    states=[]
    for i in df1.index:
        state=df1.loc[i, 'State'].split()[0]
        states.append(state)
    return states
        

zips=extract_zipcode()
states=get_state()
#print(zips)
df1['ZIP']=zips
df1['State']=states
df1


# In[155]:

# modifying columns directy
df1['State']=df1['State'] + ', ' + df1['Country']
df1['Employees']=df1['Employees'] * 2
df1


# In[156]:

df1.loc[2, 'State'].split()


# In[157]:

#  To add/manipulate rows we have to transpose!
df_t=df1.T
df_t


# In[159]:

df_t[7]=['My Address', 'My City', 'My Country', '10', 'My Shop', 'My State', 'My Continent', 'My ZIP']
df_t


# In[161]:

# Then we traspose back!
df1=df_t.T
df1


# In[163]:

# We can also modify the rows in the same way
# need to make sure we dont use '' for index or it will add a new column rathr then replace!
df_t=df1.T
df_t[3]=['332 Hill St', 'Vermont', 'Canada', '100', 'My Shop', 'My State', 'My Continent', 'My ZIP']
df_t
df1=df_t.T
df1

