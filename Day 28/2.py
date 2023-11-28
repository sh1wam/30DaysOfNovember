#Get the Size of a DataFrame
#Intuition
#The problem asks us to find the size (number of rows and columns) of a given DataFrame.

#Approach
#To solve this problem, we can use the Pandas library in Python.
#We can directly use the .shape attribute of the DataFrame to get the number of rows and columns. 
#We return the result as an array containing the number of rows and columns.

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
    # OR
    return list(players.shape)