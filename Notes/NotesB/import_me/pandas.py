import pandas as pd
import random




#Pandas series

s = [random.randrange(100) for x in range(100)]
my_series = pd.Series(s)
print(type(my_series))
print(my_series)

d = {'col1':[1,2,3], 'col2':[4,5,6]}
df = pd.DataFrame(data=d)
print(df['col1'])
print(df.describe())

