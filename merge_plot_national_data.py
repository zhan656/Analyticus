
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  merge_plot_national_data.py<p>
# <p>Input 1:  CDC Influenza-Like-Illness Json File</p>
# <p>Input 2:  HHS Vaccinations Json File</p>
# <p>Output:  plot_national.json</p>
# 

# In[ ]:


# Import dependances.
import json
import pandas as pd


# In[ ]:


# Load pandas.Dataframe from cdc_national.json
with open('data/cdc_national.json') as cdc_file:
    cdc_dict = json.load(cdc_file)


# In[ ]:


# Build a dataframe from cdc dictionary.
df = pd.DataFrame(cdc_dict)


# In[ ]:


# Build a dict from the dataframe.
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


# In[ ]:


# Build cdc dataframe from cdc dictionary.
df_cdc = pd.DataFrame(cases_dict)


# In[ ]:


# Orient attributes as column headings.
df_cdc = df_cdc.T


# In[ ]:


# Sort by week.
df_cdc = df_cdc.sort_values(['week'])


# In[ ]:


# Load hhs dictionary from hhs_national.json
with open('data/hhs_national.json') as hhs_file:
    hhs_dict = json.load(hhs_file)


# In[ ]:


# Load hhs dataframe from hhs dictionary
df_hhs = pd.DataFrame(hhs_dict)


# In[ ]:


# Sort by week.
df_hhs = df_hhs.sort_values(['week'])


# In[ ]:


# Merge the hhs and cdc dataframes.
result = pd.merge(df_cdc, df_hhs, how='outer', on=['week'])
result = result.sort_values(by=['week'])
result.fillna(0, inplace=True)


# In[ ]:


# Write the merged data to a json file.
result.to_json('data/plot_national.json')


# In[ ]:


# Sample code for accessing the merged data.
with open('data/plot_national.json') as plot_file:
    plot_dict = json.load(plot_file)


# In[ ]:


# Sample codee for accessing the merged data
df_plot = pd.DataFrame(plot_dict)
df_plot = df_plot.sort_values(['week'])
df_plot

