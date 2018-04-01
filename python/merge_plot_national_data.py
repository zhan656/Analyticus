
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  merge_plot_national_data.py<p>
# <p>Version:  March 31, 2018
# <p>Input 1:  CDC Influenza-Like-Illness Json File for Flu Season 2017</p>
# <p>Input 2:  HHS Vaccinations Json File for Flu Season 2017</p>
# <p>Output:  A json file of merged input used for plots.</p>

# In[1]:


# Import dependances.
import json
import pandas as pd


# In[2]:


# Load CDC data into a dataframe.
df = pd.read_json('../data/cdc_national.json')


# In[3]:


# Inspect the dataframe.
df.head()


# In[4]:


# Normalize CDC week to HHS week using a dictionary.
cases_dict = {}
for i in list(df.index):
    case_dict = {}
    case_dict["flu_cases"] = df.loc[i,'Cases']
    case_dict["flu_percent"] = df.loc[i, 'Percent']
    
    # Normalize CDC Week to Plot Week.
    if df.loc[i, 'Year'] == 2017:
        case_dict["week"] = df.loc[i,'Week'] - 30
    else:
        case_dict["week"] = df.loc[i,'Week'] + 22
       
    cases_dict[str(i)] = case_dict


# In[5]:


# Load the CDC dataframe from the normalized dictionary.
df_cdc = pd.DataFrame(cases_dict)


# In[6]:


# Inspect the CDC dataframe.
df_cdc.head()


# In[7]:


# Swap axis of the CDC dataframe so attributes are moved to columns.
df_cdc = df_cdc.T


# In[8]:


# Inspect the CDC dataframe.
df_cdc.head()


# In[9]:


# Sort by week to aid analysis.
df_cdc = df_cdc.sort_values(['week'])


# In[10]:


# Inspect the CDC dataframe.
df_cdc.head()


# In[11]:


# Load the HHS dataframe from the json file.
df_hhs = pd.read_json('../data/hhs_national.json')


# In[12]:


# Inspect the HHS dataframe.
df_hhs.head()


# In[13]:


# Sort by week to aid in analysis.
df_hhs = df_hhs.sort_values(['week'])


# In[14]:


# Merge the CDC and HHS data into the results dataframe.
result = pd.merge(df_cdc, df_hhs, how='outer', on=['week'])


# In[15]:


# Sort by week to aid in analysis.
result = result.sort_values(by=['week'])


# In[16]:


# Replace null values with zeroes where there is not intersection between CDC and HHS data.
result.fillna(0, inplace=True)


# In[17]:


# Inspect the result dataframe.
result.head()


# In[18]:


# Inspect the result dataframe.
result.tail()


# In[19]:


# Write the result dataframe to a json file for plots.
result.to_json('../data/plot_national.json')


# In[20]:


# Validate the file by loading it to a dataframe.
df_plot = pd.read_json('../data/hhs_national.json')


# In[21]:


# Sort the plot datafram to aid in analysis.
df_plot = df_plot.sort_values(['week'])


# In[22]:


# Validate the plot dataframe.
df_plot.head()


# In[23]:


# Validate the plot dataframe.
df_plot.tail()

