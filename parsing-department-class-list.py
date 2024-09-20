"""
started with a basic structure from
copilot to parse a json output to text file
which led to dataframes.

the rest of this i wrote myself, with
heavy googling.
"""

import json
import pandas as pd
import requests

# misc function to filter out department codes I don't care about
def is_valid_dept(code):
    if (code.startswith("ROBT")):
        return False
    elif (code.startswith("INC")):
        return False
    elif (code.startswith("K_")):
        return False
    else:
        return True

# request department list from streamer

departmentlistApi = "https://streamer.oit.duke.edu/curriculum/list_of_values/fieldname/SUBJECT?access_token=[INSERTAPIKEY]"
r = requests.get(departmentlistApi)

data = r.json()

# Extract the department info
department_info = data['scc_lov_resp']['lovs']['lov']['values']['value']

# Convert the department info to a data frame
df = pd.DataFrame(department_info)

filteredDepartments = list(filter(is_valid_dept, df["code"].tolist()))

# now, in filteredDepartments, we have our list of
# departments to query. we move to the next step, which is
# querying for the list of courses

listCoursesApi = "https://streamer.oit.duke.edu/curriculum/courses/subject/"
apiKey = "?access_token=[]"

# So for each department, we will query and save the course information in a dataframe object

aggregated_courses = []

for each in filteredDepartments:
    print(each)
    # construct the query URL
    getSubjectURL = '{}{}{}'.format(listCoursesApi, each, apiKey)
    subjectCourseList = requests.get(getSubjectURL)
    subjectClassJson = subjectCourseList.json()
    # if there aren't any courses, we can't make a dataframe this way, so we want to go back up and go to the next thing
    if subjectClassJson['ssr_get_courses_resp']['course_search_result']['subjects']['subject']['course_summaries'] is None:
        print("No courses")
    # if there's more than one class, you have a Python list, and you can turn it into a dataFrame
    elif type(subjectClassJson['ssr_get_courses_resp']['course_search_result']['subjects']['subject']['course_summaries']['course_summary']) is list:
        classInformation = subjectClassJson['ssr_get_courses_resp']['course_search_result']['subjects']['subject']['course_summaries']['course_summary']
        #subjectData = pd.DataFrame(classInformation)
        aggregated_courses = aggregated_courses + classInformation
    # if there's only one class, it's a dictionary, and you have to handle it as a pandas series
    else:
        classInformation = subjectClassJson['ssr_get_courses_resp']['course_search_result']['subjects']['subject']['course_summaries']['course_summary']
        subjectData = pd.Series(classInformation)

df_final = pd.DataFrame(aggregated_courses)

print(df_final)


