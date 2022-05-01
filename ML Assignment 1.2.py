#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


df=pd.read_csv('https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/house_rental_data.csv.txt', index_col='Unnamed: 0')
df


# In[20]:


df.isna().sum()


# In[21]:


df.duplicated().sum()


# In[22]:


df1=df.drop_duplicates()
df1


# In[23]:


df1.dtypes


# In[24]:


df1.info()


# In[25]:


df1.describe()


# # Finding the optimal value of k

# In[ ]:




