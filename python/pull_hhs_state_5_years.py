
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  pull_hhs_state_5_years.py</p>
# <p>Version:  March 31, 2018</p>
# <p>Input:  HHS Vaccinations by state from HHS API for six flu seasons.</p>
# <p>Output:  HHS Vaccinations Json File by state for six flu season.</p>

# In[1]:


# Dependencies
import requests
import json
import numpy as np
import pandas as pd


# In[2]:


# Prepare the url for retreiving the state codes used in pulling HHS data via API.
url = "https://fluvaccineapi.hhs.gov/api/v2/ids/2017/states.json"


# In[3]:


# Create a list of state codes.  Remove District of Columbia and Puerto Rico.
state_codes = requests.get(url).json()
state_codes.remove('DC')
state_codes.remove('PR')


# In[4]:


# Build a datafram of HHS data by appending data for each state within each year.
df1 = pd.DataFrame()

year_list = [2012, 2013, 2014, 2015, 2016, 2017]

for year_entry in year_list:
    
    for state_code in state_codes:
        
        url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/{}/states/{}.json?ethnicity=T&medicare_status=A".format(year_entry, state_code)
        
        state_dict = requests.get(url).json()
    
        df = pd.DataFrame(state_dict)
    
        df1 = df1.append(df, ignore_index=True)


# In[5]:


# Inspect the HHS data that was downloaded.
df1.head()


# In[6]:


# Write the downloaded data to a json file.
# This serves as a checkpoint in processing.
df1.to_json('../data/raw_hhs_state_data.json')


# In[7]:


# Load a dataframe with the downloaded data.
# This serves as a restart point in processing.
df2 = pd.read_json('../data/raw_hhs_state_data.json')


# In[8]:


# Inspect the downloaded HHS data.
df2.head()


# In[9]:


# Select only affected attributes.
df3 = df2[['count', 'percentage', 'year', 'week', 'name']]


# In[10]:


# Rename the selected attributes to match the CCD data.
df4 = df3.rename(columns={"count":"vaccinations", "percentage":"vac_percent", "name":"state"})


# In[11]:


# Sort the HHS data by year, state, and week to aid in inspection.
df5 = df4.sort_values(by=['year', 'state', 'week'])


# In[12]:


# Inspect the sorted data.
df5.head()


# In[13]:


# Add attribute "vaccination percentage by week".
df5['vac_pct_week'] = 0.0


# In[14]:


# Convert the vaccination ratio to a percentage.
df5['vac_percent'] = df5['vac_percent'] * 100


# In[15]:


# Inspect the HHS dataframe for the changes.
df5.head()


# In[16]:


# Calculate the percentage for each week by finding the difference in the culumulative percentage for consecutive weeks.
for index_entry in df5.index:
    if df5.loc[index_entry, 'week'] == 1:
        df5.loc[index_entry, 'vac_pct_week'] = df5.loc[index_entry, 'vac_percent']
    elif index_entry > 0:
        i = index_entry - 1
        df5.loc[index_entry, 'vac_pct_week'] = df5.loc[index_entry, 'vac_percent'] - df5.loc[i, 'vac_percent']


# In[17]:


# Inspect the HHS dataframe for the calculation.
df5.head()


# In[18]:


# Write the HHS data for states for five years to a json file.
df5.to_json('../data/hhs_state_5_years.json')


# In[19]:


# Validate the json file by loading it into a dataframe.
df6 = pd.read_json('../data/hhs_state_5_years.json')


# In[20]:


# Sort the HHS data by year, state, and week to aid in inspection.
df7 = df6.sort_values(['year', 'state', 'week'])


# In[21]:


# Inspect the HHS data.
df7.head()


# In[23]:


# Inspect the HHS data.
df7.tail()

