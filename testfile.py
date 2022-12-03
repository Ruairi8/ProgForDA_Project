# A .py Python file for the Programming for Data Analytics Project
# Investigating creating a custom data set manually:
import pandas as pd

# Python package pandas has the .DataFrame method which can be used to create a dataset containing key-value pairs:
dataFr = pd.DataFrame(
    {
        'column1':[1,2,3,4],
        'column2':["hello", "in", "created", "data set"],
        'col3':['John', 'Bob', 'Mia', "Tom"]
    }
)
# .head() pandas method outputs the top 10 rows of a dataset:
print(dataFr.head())
print(dataFr.shape)
# A string data type is called an object when the file is run, an integer as 'int64':
print(dataFr.dtypes)

import numpy as np
import random
x = [22, 33, 19, 18, 39, 44, 31, 74]
# 'k' sets the length of the randomly generated list from elements contained in the list, x:
ch = random.choices(x, k=5)
print(ch)
# Using weights to make some of the numbers more likely to be randomly selected:
ch2 = random.choices(x, weights=[2, 7, 2, 2, 8, 10, 6, 16], k=20)
print(ch2)

# Creating a randomly generated normal distribution centered at 20, with a standard deviation of 2 and an
# array of length 6:
y = np.random.normal(20, 2, 6)
print(y)