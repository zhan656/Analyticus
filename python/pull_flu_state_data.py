
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  pull_flu_state_data.py<p>
# <p>Version:  March 31, 2018
# <p>Input:  CDC Influenza-Like-Illness CSV File at the state level.</p>
# <p>Output:  CDC Influenza-Like_illness Json File at the state level.</p>
# <p>Description:</p>

# In[1]:


# Import dependances.
import json
import csv
import pandas as pd


# In[2]:


# Load the CDC state-level data into a dataframe.
df = pd.read_csv('../data/cdc_state.csv')


# In[3]:


# Inspect the CDC dataframe
df.head()


# In[4]:


# Write the CDC state-level data to a json file.
df.to_json('../data/cdc_state.json')


# In[5]:


# Validate the output file by loading it into a dataframe.
df2 = pd.read_json('../data/cdc_state.json')


# In[7]:


# Sort the CDC state-level data by state and week to aid analysis.
df2 = df2.sort_values(by=['State', 'Week'])


# In[8]:


# Validate CDC state-level data.
df2.head()


# In[9]:


# Validate CDC state-level data.
df2.tail()

