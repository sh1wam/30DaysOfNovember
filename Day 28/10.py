#CHANGE DATA TYPE

#Intuition
#The problem appears to ask for a solution to change the data type of a specific column ('grade') 
#in a given Pandas DataFrame named 'students' from a non-integer type to an integer type.

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We create a new DataFrame 'df' based on the 'students' DataFrame and then use the .astype() method to change the data type of the 'grade' column to integer.

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students)
    df['grade'] = df[['grade']].astype(int) # changing datatype to int.
    return df