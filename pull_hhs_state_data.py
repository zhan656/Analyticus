
# coding: utf-8

# In[1]:


# Dependencies
import requests
import json
import numpy as np


# In[2]:


# URL for GET requests to retrieve vehicle data
url = "https://fluvaccineapi.hhs.gov/api/v2/ids/2017/states.json"


# In[5]:


# Create a list of state codes.
state_codes = requests.get(url).json()
state_codes.remove('DC')
state_codes.remove('PR')


# In[7]:


# Build a dictionary of HHS state data.
state_dict = {}
state_index = 0
for state_code in state_codes:
    
    url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/2017/states/{}.json?ethnicity=T&medicare_status=A".format(state_code)
    
    state_list = requests.get(url).json()
    
    for i in np.arange(0, len(state_list)):
        state_dict[str(state_index)] = state_list[i]
        state_index += 1


# In[9]:


# Format string to be suitable for a json file.
state_str = str(state_dict)
state_str = state_str.replace("'", '"')


# In[10]:


# Write string to cdc.json
with open('data/hhs_state.json', 'w') as f:
    f.write(state_str)

