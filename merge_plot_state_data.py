
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


# Inspect the cdc dataframe.
df = df.T
df = df.sort_values(by=['year', 'week', 'state'])
# df.head()


# In[6]:


# Add vaccinations.
df['vaccinations'] = 0
df['vac_percent'] = 0


# In[7]:


# df.head()


# In[8]:


# Build a dict from the dataframe.
cases_dict = {}
for i in list(df.index):
    case_dict = {}
    case_dict["cases"] = df.loc[i,'cases']
    case_dict["flu_percent"] = df.loc[i, 'flu_percent']
    case_dict["year"] = df.loc[i,'year']
    case_dict["state"] = df.loc[i,'state']
    case_dict["week"] = df.loc[i,'week']
    case_dict["vaccinations"] = df.loc[i,'vaccinations']
    case_dict["vac_percent"] = df.loc[i,'vac_percent']
    cases_dict[str(i)] = case_dict


# In[9]:


# Format string to be suitable for a json file.
cases_str = str(cases_dict)
cases_str = cases_str.replace("'", '"')


# In[10]:


# Inspect resulting string.
# cases_str


# In[11]:


# Write string to cdc.json
with open('data/plot_state.json', 'w') as f:
    f.write(cases_str)

