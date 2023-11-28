#RENAME COLUMNS

#Intuition
#The problem appears to ask for a solution to rename specific columns in a given Pandas DataFrame named 'students'. 
#The columns to be renamed are "id" to "student_id", "first" to "first_name", "last" to "last_name", and "age" to "age_in_years".

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We can use the .rename() method on the 'students' DataFrame to rename the specified columns according to the provided mappings.

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return students