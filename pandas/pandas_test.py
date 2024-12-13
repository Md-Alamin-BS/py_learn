import pandas as pd, numpy as np

#pandas series creation

my_list = [1, 2, 3, 4, 5]   
my_series = pd.Series(my_list)
# print(my_series)
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(my_series[4])

my_index = ['A', 'B', 'C', 'D', 'E']
my_series2 = pd.Series(my_list, my_index)
my_series3 = pd.Series(my_list, index=my_index)
print(my_series2)