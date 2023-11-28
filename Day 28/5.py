#Create a New Column
#ntuition
#The problem appears to ask for a solution to create a new column named 'bonus' in a given Pandas DataFrame named 'employees'. 
#The 'bonus' column should contain values that are twice the values in the 'salary' column.

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We can use the .assign() method to create a new 'bonus' column in the 'employees' DataFrame, 
#and the values in this column can be calculated as 2 times the values in the 'salary' column.

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus=2 * employees['salary'])
    # OR
    employees['bonus'] = employees['salary'] * 2
    return employees