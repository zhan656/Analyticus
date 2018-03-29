
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
state_dict = {}
state_index = 0
for state_code in state_codes:
    
    url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/2017/states/{}.json?ethnicity=T&medicare_status=A".format(state_code)
    
    state_list = requests.get(url).json()
    
    for i in np.arange(0, len(state_list)):
        state_dict[str(state_index)] = state_list[i]
        state_index += 1


# In[ ]:


# Format string to be suitable for a json file.
state_str = str(state_dict)
state_str = state_str.replace("'", '"')


# In[ ]:


# Write string to hhs_state.json
with open('data/hhs_state.json', 'w') as f:
    f.write(state_str)


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
df_hhs = df_hhs.T
df_hhs.head()


# In[ ]:


# Sample code to access the json file.
df_hhs = df_hhs.sort_values(['week', 'name'])
df_hhs.head()

