
# coding: utf-8

# In[150]:

import pandas

# import geopy and specif which geolocator to use
from geopy.geocoders import *
gl = Nominatim()


# In[151]:

df=pandas.read_json('supermarkets.json')
df


# In[152]:

# Combine all address fields to get a full adress for geolocator
df['Address'] = df['Address'] + ', ' + df['City'] + ', ' + df['State'] + ', ' + df['Country']
df


# In[153]:

# we can use functions with dataframe's data by using ".apply"!!
df['Coordinates']=df['Address'].apply(gl.geocode)

# We can also call column without brackets :) 
df.Coordinates

# df['Longitude']=df['Coordinates'][0].latitude
# df['Longitude']


# In[154]:

# we can use functions with dataframe's data by using ".apply"!!
# First we need to create a column containing geolocated data
df['Coordinates']=df['Address'].apply(gl.geocode)

# We can then extract latitude and longitude data from this column ...
df['Latitude']=df.Coordinates.apply(lambda x: x.latitude if x != None else 'Unknown')
df['Longitude']=df.Coordinates.apply(lambda x: x.longitude if x != None else 'Unknown')

# And then drop it - and restore the address back to how it was!
df=df.drop('Coordinates', 1)
df['Address']=df.Address.apply(lambda x: x.split(',')[0])
df


# In[155]:

# Now lets fix everything else using lambda!
df['ZIP']=df.State.apply(lambda x: x.split(' ')[1] if len(x.split(' ')) > 1 else 'N/A')
df['State']=df.State.apply(lambda x: x.split(' ')[0] if len(x.split(' ')) > 1 else x)
df


# In[160]:

# And now let's save the nice version, and a different separator!
df.to_csv('shops_coordinates.sv',sep=':')

