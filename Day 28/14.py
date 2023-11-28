#RESHAPE DATA: PIVOT

#Intuition
#The problem seems to ask for a solution to pivot a given Pandas DataFrame named 'weather'. 
#The goal is to create a new DataFrame where the rows correspond to months, the columns correspond to cities, 
#and the values are the maximum temperatures for each combination of month and city.

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We use the .pivot_table() function to pivot the 'weather' DataFrame. 
#We specify 'month' as the index, 'city' as the columns, 'temperature' as the values, and 'max' as the aggregation function 
#to calculate the maximum temperature for each combination of month and city.

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot_table(
        index='month', 
        columns='city', 
        values='temperature', 
        aggfunc='max'
    )