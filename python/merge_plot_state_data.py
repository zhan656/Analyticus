
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  merge_plot_data.py<p>
# <p>Version:  March 31, 2018
# <p>Input 1:  CDC Influenza-Like-Illness Json File containing 2017 Flu Season.
# <p>Input 2:  HHS Vaccination Json File containing 2017 Flu Season.
# <p>Output:  Merged file normalized on HHS week.</p>

# In[1]:


# Import dependances.
import json
import pandas as pd
import numpy as np


# In[2]:


# Load CDC dataframe from CDC file containing state-level data for the 2017 flu season.
df = pd.read_json('../data/cdc_state.json')


# In[3]:


# Inspect the CDC dataframe.
df.head()


# In[6]:


# Sort by columns year, week, and state for processing.
df = df.sort_values(by=['Year', 'Week', 'State'])


# In[7]:


# Inspect the CDC dataframe.
df.head()


# In[8]:


# Normalize CDC week to HHS week.  
# Week 1 for HHS starts nine weeks prior to first week of CDC.
# First week of CDC is calendar week 40, which is coverted to HHS week by adjusting the week.
cases_dict = {}
for i in list(df.index):
    case_dict = {}
    case_dict["flu_cases"] = df.loc[i,'Cases']
    case_dict["flu_percent"] = df.loc[i, 'Percent']
    case_dict["state"] = df.loc[i,'State']
    
    # Normalize CDC Week to Plot Week.
    if df.loc[i, 'Year'] == 2017:
        case_dict["week"] = df.loc[i,'Week'] - 30
    else:
        case_dict["week"] = df.loc[i,'Week'] + 22
       
    cases_dict[str(i)] = case_dict


# In[9]:


# Load CDC dataframe from dictionary.
df_cdc = pd.DataFrame(cases_dict)


# In[10]:


# Inspect the CDC dataframe.
df_cdc.head()


# In[11]:


# Swap the dataframe axis so to put CDC attributes into columns.
df_cdc = df_cdc.T


# In[12]:


# Inspect the CDC dataframe.
df_cdc.head()


# In[13]:


# Load HHS dataframe from HHS file containing state-level data for the 2017 flu season.
df_hhs = pd.read_json('../data/hhs_state.json')


# In[14]:


# Inspect HHS dataframe.
df_hhs.head()


# In[15]:


# Reduce columns to those that are needed.
df_hhs = df_hhs.filter(['count','name','percentage', 'week'], axis=1)


# In[16]:


# Inspect HHS dataframe.
df_hhs.head()


# In[17]:


# Rename HHS dataframe columns to match CCD dataframe columns.
df_hhs = df_hhs.rename(columns={'count':'vaccinations', 'name':'state', 'percentage':'vac_percent'})


# In[18]:


# Inspect HHS dataframe.
df_hhs.head()


# In[19]:


# Merge CDC and HHS dataframes into a result dataframe.
result = pd.merge(df_cdc, df_hhs, how='outer', on=['state', 'week'])


# In[20]:


# Sort the result dataframe by week and state to aid analysis..
result = result.sort_values(by=['week', 'state'])


# In[21]:


# Replace null values with zeroes.
# Null values result when there is no intersection between CDC and HHS data.
result.fillna(0, inplace=True)


# In[22]:


# Inspect result dataframe.
result.head()


# In[23]:


# Inspect rsult dataframe.
result.tail()


# In[24]:


# Write the result dataframe to a json file to be used by plot modules.
result.to_json('../data/plot_state.json')


# In[25]:


# Start the validation process by pulling the plot file into a dataframe.
df_plot = pd.read_json('../data/plot_state.json')


# In[29]:


# Sort plot datafram to aid in analysis.
df_plot = df_plot.sort_values(by=['state', 'week'])


# In[30]:


# Validate plot dataframe.
df_plot.head()


# In[31]:


# Validate plot dataframe.
df_plot.tail()

