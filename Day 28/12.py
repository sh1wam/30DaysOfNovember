#RESHAPE DATA: CONCATENATE

#Intuition
#The problem seems to ask for a solution to concatenate two given Pandas DataFrames, 'df1' and 'df2', into a single DataFrame.

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We use the pd.concat() function to concatenate 'df1' and 'df2' along the rows (vertically) and return the resulting DataFrame.


import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])