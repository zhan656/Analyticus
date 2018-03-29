
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  merge_plot_data.py<p>
# <p>Input 1:  CDC Influenza-Like-Illness Json File</p>
# <p>Input 2:  HHS Vaccination Json File.</p>
# <p>Output:  plot_state.json
# <p>Description:
# <ul>
# <li>Load pandas.DataFrame from cdc_state.json file.</li>
# <li>Load dict from hhs_state.json file</li>
# <li>Loop through dict, updating dataframe with vaccination rates.
# <li>Format json string by looping through the DataFrame</li>
# <li>Write json string to plot_state.json</li>
# </ul>

# In[1]:


# Import dependances.
import json
import pandas as pd
import numpy as np


# In[2]:


# Load pandas.Dataframe from cdc.json
with open('data/cdc_state.json') as cdc_file:
    cdc_dict = json.load(cdc_file)


# In[3]:


# Inspect cdc dictionary.
# cdc_dict


# In[4]:


# Build cdc dataframe from cdc dictionary.
df = pd.DataFrame(cdc_dict)


# In[5]:


# Sort by columns year, week, and state.
df = df.sort_values(by=['Year', 'Week', 'State'])


# In[6]:


# Build a dict from the dataframe.
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


# In[7]:


# Orient columns.
df_cdc = pd.DataFrame(cases_dict)
df_cdc = df_cdc.T


# In[8]:


# Load pandas.Dataframe from hhs_state.json
with open('data/hhs_state.json') as hhs_file:
    hhs_dict = json.load(hhs_file)


# In[9]:


# Create HHS dataframe from HHS dictionary.
df_hhs = pd.DataFrame(hhs_dict)
df_hhs = df_hhs.T
# df_hhs.head()


# In[10]:


# Reduce columns to those that are needed.
df_hhs = df_hhs.filter(['count','name','percentage', 'week'], axis=1)
# df_hhs.head()


# In[11]:


# Rename HHS dataframe columns to match CCD dataframe columns.
df_hhs = df_hhs.rename(columns={'count':'vaccinations', 'name':'state', 'percentage':'vac_percent'})
# df_hhs.head()


# In[12]:


# Merge with outer join the HHS and CDC dataframes.
result = pd.merge(df_cdc, df_hhs, how='outer', on=['state', 'week'])
result = result.sort_values(by=['week', 'state'])
result.fillna(0, inplace=True)
# result


# In[13]:


# Write the merged datafram to the json file.
result.to_json('data/plot_state.json')


# In[14]:


# Sample code to access the json file.
with open('data/plot_state.json') as plot_state_file:
    plot_state_dict = json.load(plot_state_file)


# In[15]:


# Sample code to access the json file.
df_plot_state = pd.DataFrame(plot_state_dict)
df_plot_state = df_plot_state.sort_values(by=['week', 'state'])
df_plot_state.head()


# In[16]:


# Sample code to access the json file.
# df_plot_state

