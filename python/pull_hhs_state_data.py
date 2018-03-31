
# coding: utf-8

# In[ ]:


# Dependencies
import requests
import json
import numpy as np
import pandas as pd


# In[ ]:


# URL for GET requests to retrieve vehicle data
url = "https://fluvaccineapi.hhs.gov/api/v2/ids/2017/states.json"


# In[ ]:


# Create a list of state codes.
state_codes = requests.get(url).json()
state_codes.remove('DC')
state_codes.remove('PR')


# In[ ]:


# Build a dictionary of HHS state data.
results = []
for state_code in state_codes:
    
    url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/2017/states/{}.json?ethnicity=T&medicare_status=A".format(state_code)
    
    state_list = requests.get(url).json()
    
    for i in np.arange(0, len(state_list)):
        results.append(state_list[i])


# In[ ]:


df = pd.DataFrame(results)


# In[ ]:


# Inspect dataframe
# df.head()


# In[ ]:


df.to_json('data/hhs_state.json')


# In[ ]:


# Sample code to access the json file.
with open('data/hhs_state.json') as hhs_state_file:
    hhs_state_dict = json.load(hhs_state_file)


# In[ ]:


# Sample code to access the json file.
df_hhs = pd.DataFrame(hhs_state_dict)
df_hhs.head()


# In[ ]:


# Sample code to access the json file.
# df_hhs = df_hhs.sort_values(['week', 'name'])
# df_hhs

