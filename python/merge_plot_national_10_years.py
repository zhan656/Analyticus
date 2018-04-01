
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  merge_plot_national_10_years.py<p>
# <p>Version:  March 31, 2018
# <p>Input 1:  CDC Influenza-Like-Illness Json File containing ten years of data.</p>
# <p>Input 2:  HHS Vaccinations Json File containing five years of data.</p>
# <p>Output:  Merged inputs based on year (flu season) and week (normalized to HHS week).
# 

# In[1]:


# Import dependances.
import json
import pandas as pd


# In[2]:


# Load pandas.Dataframe from cdc_national.json
df_cdc = pd.read_json('../data/cdc_national_10_years.json')


# In[3]:


# Sort to aid in analysis.
df_cdc = df_cdc.sort_values(by=['YEAR', 'WEEK'])


# In[4]:


# Rename columns to names common to both input files to facilitate the merge.
df_cdc = df_cdc.rename(columns={"FLU_PERCENT":"flu_percent", "ILITOTAL":"flu_cases", "WEEK":"week", "YEAR":"year"})


# In[5]:


# Verify the CDC dataframe.
df_cdc.head()


# In[6]:


# Verify the CDC dataframe.
df_cdc.tail()


# In[7]:


# Load HHS dataframe.
df_hhs = pd.read_json('../data/hhs_national_10_years.json')


# In[8]:


# Order by year and week to aid in analysis.
df_hhs = df_hhs.sort_values(by=['year', 'week'])


# In[9]:


# Verify the HHS dataframe.
df_hhs.head()


# In[10]:


# Verify the HHS dataframe.
df_hhs.tail()


# In[11]:


# Merge the CDC and HHS dataframes on year and week.
df = pd.merge(df_cdc, df_hhs, how='outer', on=['year', 'week'])


# In[12]:


# Sort by year and week to aid in analysis.
df = df.sort_values(by=['year', 'week'])


# In[13]:


# Replace the null values with zero.
# This occurs when there is not an intersection of HHS or CDC.
df.fillna(0, inplace=True)


# In[14]:


# Check the dataframe containing the merged data.
df.head()


# In[15]:


# Check the datafrme containing the merged data.
df.tail()


# In[16]:


# Write the merged data to a json file.
df.to_json('../data/plot_national_10_years.json')


# In[17]:


# Read the json file of merged data for validation.
df_plot = pd.read_json('../data/plot_national_10_years.json')


# In[18]:


# Sort the plot data to aid in analysis.
df_plot = df_plot.sort_values(['year', 'week'])


# In[19]:


# Validate plot data.
df_plot.head()


# In[20]:


# Validate plot data.
df_plot.tail()

