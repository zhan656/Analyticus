
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

# In[ ]:


# Import dependances.
import json
import csv
import pandas as pd


# In[ ]:


# Load pandas.Dataframe from cdc.csv.
df = pd.read_csv('data/cdc_state.csv')


# In[ ]:


# Inspect dataframe
df.head()


# In[ ]:


df.to_json('data/cdc_state.json')


# In[ ]:


# Sample code to access the json file.
with open('data/cdc_state.json') as cdc_state_file:
    cdc_state_dict = json.load(cdc_state_file)


# In[ ]:


# Sample code to access the json file.
df_cdc_state = pd.DataFrame(cdc_state_dict)
df_cdc_state = df_cdc_state.sort_values(by=['Year', 'Week', 'State'])
df_cdc_state.head()


# In[ ]:


# Inspect resulting string.
# df_cdc_state

