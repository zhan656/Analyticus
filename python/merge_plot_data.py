
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  merge_plot_data.py<p>
# <p>Input 1:  CDC Influenza-Like-Illness Json File</p>
# <p>Input 2:  Twitter Influenza-Like-Illness Json File</p>
# <p>Output:  plot.json
# <p>Description:
# <ul>
# <li>Load pandas.DataFrame from cdc.json file.</li>
# <li>Load dict from twitter.json file</li>
# <li>Loop through dict, updating dataframe with tweets.
# <li>Format json string by looping through the DataFrame</li>
# <li>Write json string to plot.json</li>
# </ul>

# In[1]:


# Import dependances.
import json
import csv
import pandas as pd


# In[2]:


# Load pandas.Dataframe from cdc.json
with open('cdc.json') as cdc_file:
    cdc_dict = json.load(cdc_file)


# In[3]:


# Inspect cdc dictionary.
# cdc_dict


# In[4]:


# Build cdc dataframe from cdc dictionary.
df = pd.DataFrame(cdc_dict)


# In[5]:


# Inspect the cdc dataframe.
df = df.T
df = df.sort_values(by=['year', 'week', 'state'])
# df.head()


# In[6]:


# Add tweets
df['tweets'] = 0
# df.head()


# In[7]:


# Build a dict from the dataframe.
cases_dict = {}
for i in list(df.index):
    case_dict = {}
    case_dict["cases"] = df.loc[i,'cases']
    case_dict["year"] = df.loc[i,'year']
    case_dict["state"] = df.loc[i,'state']
    case_dict["week"] = df.loc[i,'week']
    case_dict["tweets"] = df.loc[i,'tweets']
    cases_dict[str(i)] = case_dict


# In[8]:


# Format string to be suitable for a json file.
cases_str = str(cases_dict)
cases_str = cases_str.replace("'", '"')


# In[9]:


# Inspect resulting string.
# cases_str


# In[10]:


# Write string to cdc.json
with open('plot.json', 'w') as f:
    f.write(cases_str)

