
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  pull_flu_data.py<p>
# <p>Input:  CDC Influenza-Like-Illness CSV File:  cdc_national.csv</p>
# <p>Output:  cdc_national.json
# <p>Description:
# <ul>
# <li>Load pandas.DataFrame from cdc_national.csv file.</li>
# <li>Format json string by looping through the DataFrame</li>
# <li>Write json string to cdc_national.json</li>
# </ul>

# In[1]:


# Import dependances.
import json
import csv
import pandas as pd


# In[2]:


# Load pandas.Dataframe from cdc.csv.
df = pd.read_csv('data/cdc_national.csv')


# In[3]:


# Inspect dataframe
df.head()


# In[4]:


# Write string to cdc.json
df.to_json('data/cdc_national.json')

