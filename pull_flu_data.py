
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  pull_flu_data.py<p>
# <p>Input:  CDC Influenza-Like-Illness CSV File</p>
# <p>Output:  cdc.json
# <p>Description:
# <ul>
# <li>Load pandas.DataFrame from cdc.csv file.</li>
# <li>Format json string by looping through the DataFrame</li>
# <li>Write json string to cdc.json</li>
# </ul>

# In[1]:


# Import dependances.
import json
import csv
import pandas as pd


# In[2]:


# Load pandas.Dataframe from cdc.csv.
df = pd.read_csv('cdc.csv')


# In[3]:


# Inspect dataframe
# df.head()


# In[4]:


# Build a dict from the dataframe.
cases_dict = {}
for i in list(df.index):
    case_dict = {}
    case_dict["cases"] = df.loc[i,'Cases']
    case_dict["year"] = df.loc[i,'Year']
    case_dict["state"] = df.loc[i,'State']
    case_dict["week"] = df.loc[i,'Week']
    cases_dict[str(i)] = case_dict


# In[5]:


# Format string to be suitable for a json file.
cases_str = str(cases_dict)
cases_str = cases_str.replace("'", '"')


# In[6]:


# Inspect resulting string.
# cases_str


# In[7]:


# Write string to cdc.json
with open('cdc.json', 'w') as f:
    f.write(cases_str)

