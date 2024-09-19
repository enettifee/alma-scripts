'''
Saving this as an example (generated from Microsoft Copilot - e.g., I did not write this) on parsing data
from the OIT Streamer curriculum API.
'''

import json
import pandas as pd

# Load the JSON data from the file
with open('cultural-anthropology.json', 'r') as file:
    data = json.load(file)

# Extract the course summaries
course_summaries = data['ssr_get_courses_resp']['course_search_result']['subjects']['subject']['course_summaries']['course_summary']

# Convert the course summaries to a DataFrame
df = pd.DataFrame(course_summaries)

# Save the DataFrame to a text file in tabular format
df.to_csv('cultural_anthropology_courses.txt', sep='\t', index=False)

print("The JSON data has been converted to tabular format and saved to 'cultural_anthropology_courses.txt'.")
