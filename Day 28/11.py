#FILL MISSING DATA

#Intuition
#The problem seems to ask for a solution to fill missing values in the 'quantity' column
#of a given Pandas DataFrame named 'products' with zeros.

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We use the .fillna() method on the 'quantity' column of the 'products' DataFrame to replace missing values with zeros.

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products