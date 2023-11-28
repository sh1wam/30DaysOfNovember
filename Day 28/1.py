#Create a DataFrame from List
#Intuition
#The problem asks us to create a DataFrame from a given 2D list containing student IDs and ages. 
#We need to ensure that the DataFrame has two columns named 'student_id' and 'age' 
#and is in the same order as the original 2D list.

#Approach
#To solve this problem, we can use the Pandas library in Python. 
#We first define the column names as 'student_id' and 'age', 
#and then create a DataFrame using the provided student_data and these column names.

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names = ['student_id', 'age']
    result = pd.DataFrame(student_data, columns=column_names)
    return result 