#Display the First Three Rows
#Intuition
#The problem appears to require a solution to select and return the first three rows of a given Pandas DataFrame named 'employees'.

#Approach
#To address this problem, we utilize the Pandas library in Python. 
#Specifically, we employ the .head(3) method, 
#which enables us to select and return the first three rows of the 'employees' DataFrame.

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)