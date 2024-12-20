import pandas as pd, numpy as np

#pandas series creation

my_list = [1, 2, 3, 4, 5]   
my_series = pd.Series(my_list)
# print(my_series)
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(my_series[4])

my_index = ['A', 'B', 'C', 'D', 'E']
my_series2 = pd.Series(my_list, my_index)
my_series3 = pd.Series(my_list, index=my_index) #Also index can be used here this way: index=['A', 'B', 'C', 'D', 'E']
print(my_series2)
print(my_series3['C'])
# print(my_series2[2]) #this is depricated

# Dictionary to Series
cars = {'BMW': 5, 'Audi': 3, 'Mercedes': 7, 'Toyota': 2, 'Ford': 1}
cars_series = pd.Series(cars)
print(cars_series)
print(cars_series['Audi'])
print(cars_series.iloc[1])

# Add specific item to series from dictionary
cars_series2 = pd.Series(cars, index=['BMW', 'Mercedes', 'Toyota'])
print(cars_series2)