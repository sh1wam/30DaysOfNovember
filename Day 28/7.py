#Drop Missing Data

#Intuition
#The problem appears to ask for a solution to remove rows with missing values in a specific column ('name') 
#in a given Pandas DataFrame named 'students'.

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We can use the .notnull() method on the 'name' column of the 'students' DataFrame 
#to identify rows with non-null values in the 'name' column. 
#Then, we can create a new DataFrame containing only those rows.

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(students)[students['name'].notnull()]