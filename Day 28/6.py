#Drop Duplicate Rows

#Intuition
#The problem appears to ask for a solution to remove duplicate rows from a given Pandas DataFrame 
#named 'customers' based on the 'email' column.

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We use the .drop_duplicates() method on the 'customers' DataFrame to remove duplicate rows based on the 'email' column.
# The subset parameter specifies the column to consider for duplicates. 
#The default behavior is to keep the first occurrence of each duplicate and remove the subsequent ones.

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

    # OR

    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers