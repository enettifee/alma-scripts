'''
Saving this as an example (generated from Microsoft Copilot - e.g., I did not write this) on parsing data
from the OIT Streamer curriculum API.
'''

import json
import pandas as pd
import requests

# request department list from streamer

departmentlistApi = "https://streamer.oit.duke.edu/curriculum/list_of_values/fieldname/SUBJECT?access_token=[INSERTAPIKEY]"

r = requests.get(departmentlistApi)
data = r.json()

# Extract the department info
department_info = data['scc_lov_resp']['lovs']['lov']['values']['value']

# Convert the department info to a data frame
df = pd.DataFrame(department_info)

print(df)
