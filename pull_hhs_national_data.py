
# coding: utf-8

# In[ ]:


# Dependencies
import requests
import json
import numpy as np
import pandas as pd


# In[ ]:


# Build a dictionary of HHS national data.    
url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/2017/national.json?ethnicity=T&medicare_status=A"
    
national_dict = requests.get(url).json()


# In[ ]:


df = pd.DataFrame(national_dict)


# In[ ]:


df = df[['count', 'percentage', 'week']]


# In[ ]:


df = df.rename(columns={"count":"vaccinations", "percentage":"vac_percent"})


# In[ ]:


df.to_json('data/hhs_national.json')


# In[ ]:


# Sample code to access the json file.
with open('data/hhs_national.json') as hhs_national_file:
    hhs_national_dict = json.load(hhs_national_file)


# In[ ]:


# Sample codee for accessing the merged data
df_hhs = pd.DataFrame(hhs_national_dict)
df_hhs = df_hhs.sort_values(['week'])
df_hhs

