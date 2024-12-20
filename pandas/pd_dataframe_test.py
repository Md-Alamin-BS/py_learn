import pandas as pd, numpy as np
from numpy.random import randn

# Create a DataFrame
my_data = randn(4, 3)
# print(my_data)
my_rows = ['A', 'B', 'C', 'D']
my_cols = ['Monday', 'Tuesday', 'Friday']

my_df = pd.DataFrame(my_data, my_rows, my_cols)
# print (my_df)

my_csv_df = pd.read_csv('C:/Users/BS01395/Documents/GitHub/py_learn/pandas/sample_data.csv')
print(my_csv_df)
print(my_csv_df.loc[0])
# print(my_csv_df.iloc[1])
print(my_csv_df['Name'])
print(my_csv_df[['Name', 'Age']])
print(my_csv_df['Age'].mean())
print(my_csv_df['Age'].max())
print(my_csv_df.iloc[[3, 4], [0, 3]])
print(my_csv_df.loc[my_csv_df['Age'] > 30])
print(my_csv_df.loc[(my_csv_df['Age'] > 30) & (my_csv_df['Age'] < 40)])
print(my_csv_df.iloc[(my_csv_df[2] > 30)])