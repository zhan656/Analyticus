
# coding: utf-8

# <p>Class:  USC Viterbi Data Analytics Bootcamp</p>
# <p>Team:  Analyticus (aka Team 5)</p>
# <p>Module:  pull_cdc_national_10_years.py<p>
# <p>Version:  March 31, 2018
# <p>Input:  CDC Influenza-Like-Illness CSV File containing ten years of data.</p>
# <p>Output:  CDC json file containing ten years of CDC data normalized to HHS flu season.</p>

# In[2]:


# Import dependances.
import json
import csv
import pandas as pd


# In[3]:


# Load CDC data into a dataframe.
df = pd.read_csv('../data/cdc_national_10_years.csv', skiprows=[0])


# In[4]:


# Validate the CDC dataframe.
df.head()


# In[6]:


# Sort the data into year, week, total sequence to aid analysis.
df2 = df[['YEAR', 'WEEK', 'ILITOTAL']]


# In[7]:


# Inspect the data.
df2.head()


# In[8]:


# Inspect the data.
df2.tail()


# In[9]:


# Normalize the CDC year and week to HHS year and week.
df3 = pd.DataFrame()
for df2_index in df2.index:
    if df2.loc[df2_index, 'WEEK'] > 39:
        df3.loc[df2_index, 'YEAR'] = df2.loc[df2_index, 'YEAR']
        df3.loc[df2_index, 'WEEK'] = df2.loc[df2_index, 'WEEK'] - 39
    else:
        df3.loc[df2_index, 'WEEK'] = df2.loc[df2_index, 'WEEK'] + 13
        df3.loc[df2_index, 'YEAR'] = df2.loc[df2_index, 'YEAR'] - 1
    df3.loc[df2_index, 'ILITOTAL'] = df2.loc[df2_index, 'ILITOTAL']
    


# In[10]:


# Inspect the normalized data.
df3.head()


# In[11]:


# Sort the normalized data to aid analysis.
df4 = df3.sort_values(['YEAR', 'WEEK'])


# In[12]:


# Inspect the data.
df4.head()


# In[13]:


# Inspect the data.
df4.tail()


# In[14]:


# Convert year and week from type float to type int.
df5 = df4.loc[:,['YEAR', 'WEEK','ILITOTAL']].astype(int)


# In[15]:


# Inspect the year and week integers.
df5.head()


# In[17]:


# Calculate total flu cases by year.  
# The sum will be used for calculating percentages.
df6 = pd.DataFrame(df5.groupby('YEAR').agg({'ILITOTAL': 'sum'}))


# In[18]:


# Inspect the cases sums by year.
df6.head()


# In[19]:


# Check the code needed to access the case sum.
df6.columns
df6.loc[2011, 'ILITOTAL']


# In[20]:


# Calculate the case percentage by dividing the week cases by the sum of cases for the year.
for df5_index in df5.index:
    df6_index = df5.loc[df5_index, 'YEAR']
    df5.loc[df5_index, 'FLU_PERCENT'] = (df5.loc[df5_index, 'ILITOTAL'] / df6.loc[df6_index, 'ILITOTAL']) * 100


# In[21]:


# Verify that the case percentages for a year add to 100 percent.
pd.DataFrame(df5.groupby('YEAR').agg({'FLU_PERCENT': 'sum'}))


# In[22]:


# Write the data to a json file.
df5.to_json('../data/cdc_national_10_years.json')


# In[24]:


# Load a dataframe with data from the just-written file for validation.
df7 = pd.read_json('../data/cdc_national_10_years.json')


# In[26]:


# Sort the data to aid validation.
df8 = df7.sort_values(by=['YEAR', 'WEEK'])


# In[27]:


# Validate CDC data.
df8.head()


# In[28]:


# Validate CDC data.
df8.tail()

