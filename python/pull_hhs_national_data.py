
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  pull_hhs_national_data.py</p>
# <p>Version:  March 31, 2018</p>
# <p>Input:  HHS Vaccinations from HHS API for flu season 2017.</p>
# <p>Output:  HHS Vaccinations Json File for flu season 2017.</p>

# In[1]:


# Dependencies
import requests
import json
import numpy as np
import pandas as pd


# In[2]:


# Load a dictionary from the HHS website. 
url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/2017/national.json?ethnicity=T&medicare_status=A"
    
national_dict = requests.get(url).json()


# In[3]:


# Load a dataframe with HHS data from the dictionary.
df = pd.DataFrame(national_dict)


# In[4]:


# Inspect the HHS dataframe.
df.head()


# In[5]:


# Select only columns count, percentage, and week.
df = df[['count', 'percentage', 'week']]


# In[6]:


# Rename columns to match CDC data.
df = df.rename(columns={"count":"vaccinations", "percentage":"vac_percent"})


# In[7]:


# Create another dataframe.
# This is a checkpoint for restarting the process.
df2 = df


# In[8]:


# Inspect the HHS dataframe.
df2.head()


# In[9]:


# Convert the vacination percentage from a ratio to a percentage.
df2.vac_percent = df2.vac_percent * 100


# In[10]:


# Inspect the dataframe for the change.
df2.head()


# In[11]:


# Add the "vaccination percentage per week" attribute.
df2['vac_pct_week'] = 0.0


# In[12]:


# Calculate the vaccination per week by getting the differences in the cumulative vaccine rate.
for index_entry in df2.index:
    if index_entry == 0:
        df2.loc[index_entry, 'vac_pct_week'] = df2.loc[index_entry, 'vac_percent']
        continue
    i = index_entry - 1
    df2.loc[index_entry, 'vac_pct_week'] = df2.loc[index_entry, 'vac_percent'] - df2.loc[i, 'vac_percent']


# In[13]:


# Inspect the HHS dataframe for the calculation.
df2.head()


# In[14]:


# Write the HHS national data to a json file.
df2.to_json('../data/hhs_national.json')


# In[16]:


# Start the validation process by loading the above file into a dataframe.
df3 = pd.read_json('../data/hhs_national.json')


# In[18]:


# Sort the HHS dataframe by week to aid in inspection.
df4 = df3.sort_values(['week'])


# In[19]:


# Inspect HHS data.
df4.head()


# In[20]:


# Inspect HHS data.
df4.tail()

