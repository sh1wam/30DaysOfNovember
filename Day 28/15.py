#METHOD CHAINING

#Intuition
#The problem appears to ask for a solution to find and return the names of animals in a given Pandas DataFrame named 'animals' 
#that have a weight greater than 100.

#Approach
#To solve this problem, we can utilize the Pandas library in Python. 
#We first sort the 'animals' DataFrame in descending order based on the 'weight' column using the .sort_values() method. 
#Then, we use boolean indexing to select rows where the 'weight' is greater than 100 and extract the 'name' column.

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals.sort_values(by='weight', ascending=False)
    return animals.loc[animals["weight"] > 100, ['name']]