#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')
import requests
import json
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import requests 
from scipy import stats
import seaborn as sns
from Scott_keys import yelpkey


# In[15]:


# import Ryan's delivery data

delivery_data = pd.read_csv("delivery_dataframe_run.csv")
delivery_df = pd.DataFrame(delivery_data)
delivery_df.head()


# In[16]:


# format the % deliver column to match % no cars

delivery_df['% That Deliver'] = (delivery_df['% That Deliver'] * 100).map('{:,.1f}'.format)
delivery_df.head()


# In[17]:


# check data types
delivery_df.dtypes


# In[18]:


# convert % deliver to float data type
delivery_df['% That Deliver'] = delivery_df['% That Deliver'].astype(float)
delivery_df.dtypes


# In[36]:


slope, intercept, r_value, p_value, std_err = stats.linregress(delivery_df['% That Deliver'], delivery_df['% No Cars'])
print(p_value)


# In[105]:


plt.figure(figsize=(10,10))
plt.plot(delivery_df['% That Deliver'], delivery_df['% No Cars'], 'o', color= '#666666', alpha=.5, label='zip codes', markersize=10)
plt.plot(delivery_df['% That Deliver'], intercept + slope*(delivery_df['% That Deliver']), color='#00CC99', label='fitted line')
plt.legend()
plt.ylim([0,100]) 
plt.xlim([0,100])
plt.title("Delivery Restaurants vs Vehicle Ownership",fontsize=20, fontweight="bold")
plt.xlabel("% Restaurants That Deliver",fontsize=16)
plt.ylabel("% Households Without Vehicles",fontsize=16)
plt.show()


# In[92]:


# plot data

delivery_df.plot(kind='scatter',x='% That Deliver',y='% No Cars',color='red', figsize=(10,10))

plt.title("Delivery Restaurant vs Vehicles",fontsize=16, fontweight="bold")
plt.xlabel("% Restaurants That Deliver",fontsize=16)
plt.ylabel("% Households Without Vehicles",fontsize=16)
plt.ylim([0,100]) 
plt.xlim([0,100]) 

plt.show()

plt.savefig("Delivery_Scatter_Regression.png")


# In[37]:


sns.lmplot(x='% That Deliver',y='% No Cars',data=delivery_df,fit_reg=True) 


# In[37]:


# save plot as png

# plt.savefig("Delivery_Scatter.png")


# In[ ]:




