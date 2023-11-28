#Select Data
#Intuition
#The problem suggests that we need to create a solution to select and return specific columns (name and age) 
#from a given Pandas DataFrame named 'students' where the 'student_id' is equal to 101.

#Approach
#To address this problem, we utilize the Pandas library in Python. 
#We employ DataFrame indexing and selection techniques to filter the rows where the 'student_id' is equal to 101. 
#Then, we select only the "name" and "age" columns from the filtered DataFrame.

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id == 101][["name", "age"]]