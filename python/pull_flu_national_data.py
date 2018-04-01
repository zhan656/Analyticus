
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  pull_flu_national_data.py<p>
# <p>Version:  March 31, 2018
# <p>Input:  CDC Influenza-Like-Illness CSV File:  cdc_national.csv</p>
# <p>Output:  cdc_national.json</p>

# In[1]:


# Import dependances.
import json
import csv
import pandas as pd


# In[3]:


# Load a dataframe with national CDC data.
df = pd.read_csv('../data/cdc_national.csv')


# In[4]:


# Inspect the dataframe with the CDC national data.
df.head()


# In[5]:


# Write the CDC data to a json file.
df.to_json('../data/cdc_national.json')


# In[8]:


# Validate the json by loading it into a dataframe for inspection.
df2 = pd.read_json('../data/cdc_national.json')


# In[9]:


# Validate the CDC data.
df2.head()


# In[10]:


# Validate the CDC data.
df2.tail()

