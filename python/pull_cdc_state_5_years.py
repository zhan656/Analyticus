
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  pull_cdc_state_5_years.py</p>
# <p>Version:  March 31, 2018
# <p>Input:  CDC Influenza-Like-Illness CSV File for last five flu seasons.</p>
# <p>Output:  CDC json file with flu cases for the last five flu seasons.</p>

# In[1]:


# Import dependances.
import json
import csv
import pandas as pd


# In[2]:


# Load CDC data into a dataframe.
df = pd.read_csv('../data/cdc_state_5_years.csv', skiprows=[0])


# In[3]:


# Inspect the dataframe.
df.head()


# In[4]:


# Select only columns needed.
df2 = df[['YEAR', 'WEEK', 'REGION', 'ILITOTAL']]


# In[5]:


# Inspect dataframe
df2.head()


# In[6]:


# Normalize CDC year and weeks to HHS year and weeks.
df3 = pd.DataFrame()
for df2_index in df2.index:
    if df2.loc[df2_index, 'WEEK'] > 39:
        df3.loc[df2_index, 'YEAR'] = df2.loc[df2_index, 'YEAR']
        df3.loc[df2_index, 'WEEK'] = df2.loc[df2_index, 'WEEK'] - 39
    else:
        df3.loc[df2_index, 'WEEK'] = df2.loc[df2_index, 'WEEK'] + 13
        df3.loc[df2_index, 'YEAR'] = df2.loc[df2_index, 'YEAR'] - 1
    df3.loc[df2_index, 'REGION'] = df2.loc[df2_index, 'REGION']
    if df2.loc[df2_index, 'ILITOTAL'] == 'X':
        df3.loc[df2_index, 'ILITOTAL'] = 0
    else:
        df3.loc[df2_index, 'ILITOTAL'] = df2.loc[df2_index, 'ILITOTAL']
    


# In[7]:


# Inspect the dataframe.
df3.head()


# In[8]:


# Sort the CDC dataframe into year, week, and region sequence to aid analysis.
df4 = df3.sort_values(['YEAR', 'WEEK', 'REGION'])


# In[9]:


# Inspect CDC dataframe.
df4.head()


# In[10]:


# Create a save point to avoiding the current dataframe.
df5 = df4


# In[11]:


# Change the type for year and week to type integer.
df5['YEAR'] = df5['YEAR'].astype(int)
df5['WEEK'] = df5['WEEK'].astype(int)
df5['ILITOTAL'] = df5['ILITOTAL'].astype(int)


# In[12]:


# Check for type integer for year and week.
df5.head()


# In[13]:


# Calculate total flu cases per state per year.
# This divided into the flu cases per state per week will give the percent flu for the week.
df6 = pd.DataFrame(df5.groupby(['YEAR','REGION']).agg({'ILITOTAL': 'sum'}))


# In[15]:


# Inspect the sum of flu cases per year per state.
df6.head()


# In[16]:


# Calculate the percent flu cases per week for the year for each state.
for df5_index in df5.index:
    
    year_index = df5.loc[df5_index, 'YEAR']
    region_index = df5.loc[df5_index, 'REGION']
    
    state_total = df6.loc[year_index].loc[region_index][0]
    
    if state_total > 0:
        df5.loc[df5_index, 'FLU_PERCENT'] = (df5.loc[df5_index, 'ILITOTAL'] / state_total) * 100
    else:
        df5.loc[df5_index, 'FLU_PERCENT'] = 0.0


# In[18]:


# Validate the calculation by inspecting Alabama for 2013.
df7 = df5.loc[(df5['REGION'] == 'Alabama') & (df5['YEAR'] == 2013)]


# In[19]:


# Inspect dataframe for Alabama 2013.
df7.head()


# In[21]:


# Add up the calculated flu percentages for Alabama 2013.
df8 = pd.DataFrame(df7.groupby(['YEAR']).agg({'FLU_PERCENT': 'sum'}))


# In[22]:


# One hundred percent indicates all the calculated percentages add up correctly.
df8


# In[23]:


# Inspect the CDC dataframe.
df5.head()


# In[24]:


# Rename the CDC dataframe columns to match the HHS columns.
df9 = df5.rename(columns = {"YEAR":"year", "WEEK":"week", "REGION":"state", "ILITOTAL":"flu_cases", "FLU_PERCENT":"flu_percent"})


# In[25]:


# Inspect the new column names.
df9.head()


# In[26]:


# Write the CDC dataframe to a json file to be used by the plot modules.
df9.to_json('../data/cdc_state_5_years.json')


# In[27]:


# Begin the validation of the file just written by loading it into a dataframe.
dfA = pd.read_json('../data/cdc_state_5_years.json')


# In[28]:


# Sort the CDC data by year, state, and week to aid in inspection.
dfB = dfA.sort_values(by=['year', 'state', 'week'])


# In[29]:


# Validate CDC data.
dfB.head()


# In[31]:


# Validate CDC data.
dfB.tail()

