# A .py Python file for the Programming for Data Analytics Project
# Investigating creating a custom data set manually:
import pandas as pd

dataFr = pd.DataFrame(
    {
        'column1':[1,2,3,4],
        'column2':["hello", "in", "created", "data set"],
        'col3':['John', 'Bob', 'Mia', "Tom"]
    }
)
print(dataFr.head())
print(dataFr.shape)
# A string data type is called an object when the file is run, an integer as 'int64':
print(dataFr.dtypes)

import numpy as np
import random
x = [22, 33, 19, 18, 39, 44, 31, 74]
# 'k' sets the length of the randomly generated list:
ch = random.choices(x, k=5)
print(ch)
# Using weights to make some of the numbers more likely to be randomly selected:
ch2 = random.choices(x, weights=[2, 7, 2, 2, 8, 10, 6, 16], k=20)
print(ch2)

y = np.random.normal(20, 2, 6)
print(y)