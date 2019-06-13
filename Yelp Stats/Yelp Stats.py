#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Import the modules
import requests
import json
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import requests 
import scipy.stats as stats
import random
import folium
from uszipcode import SearchEngine


# In[2]:


delivery_data = "delivery_dataframe_run.csv"
delivery_df = pd.read_csv(delivery_data)
delivery_df.head()


# In[3]:


#calculate the population mean for places that deliver in a specific zip code
population1 = delivery_df[delivery_df["Zip Code"] == 10019]
population1.mean()


# In[4]:


#calculate the population mean for places that deliver in a specific zip code
population1 = delivery_df[delivery_df["Zip Code"] == 10004]
population1.mean()


# In[5]:


#calculate the population mean for places that deliver in a specific zip code
population1 = delivery_df[delivery_df["Zip Code"] == 10034]
population1.mean()


# In[6]:


delivery_df.set_index('Zip Code', drop=True, inplace=True)
delivery_df


# In[ ]:





# In[7]:


# Create random indices representing
# a user's choice of posts
sample = delivery_df.sample(10)
sample


# In[8]:


#ANOVA ANALYSIS OF VARIANCE
#Create a boxplot to compare means
sample.plot.bar(y='# Pizza/Chinese Restaurants')


# In[9]:


search = SearchEngine(simple_zipcode=True)
#coordinates = [search.by_zipcode(zipcode).to_json() 
zip_dict = {}
for zipcode in delivery_df.index.values:
    tempDict = search.by_zipcode(zipcode).to_dict()
    zip_dict.update({zipcode: [tempDict['lat'], tempDict['lng']]})
zip_dict


# In[ ]:





# In[12]:



folium_map = folium.Map(location=[40.7128, -74.0060],
                        zoom_start=13,
                         tiles="CartoDB dark_matter")

for key in zip_dict:
# radius of circles
    # choose the color of the marker
    if int(delivery_df.loc[key, "# Pizza/Chinese Restaurants"])>30:
        color="#39cc28" # green
    elif int(delivery_df.loc[key, "# Pizza/Chinese Restaurants"])>20:
        color="#2743cc" #blue
    else:
        color="#ea1f09" # green
    radius = int(delivery_df.loc[key, "# Pizza/Chinese Restaurants"]/2)
    marker = folium.CircleMarker(location=zip_dict[key],
                                 radius=radius,
                                 color=color).add_to(folium_map)

folium_map


# In[ ]:


plt.figure(figsize=(13,10), dpi= 80)
sns.distplot(delivery_df[sample.loc[delivery_df['zip_dict']]==[key, "# Pizza/Chinese Restaurants"]])
plt.ylim(0, 0.35)


# In[ ]:





# In[ ]:





# In[ ]:




