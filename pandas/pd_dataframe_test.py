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
# print(my_csv_df)
# print(my_csv_df.columns)
# print(my_csv_df.loc[0])
# print(my_csv_df.iloc[1])
# print(my_csv_df['Name'])
# print(my_csv_df[['Name', 'Age']])
# print(my_csv_df['Age'].mean())
# print(my_csv_df['Age'].max())
# print(my_csv_df.iloc[[3, 4], [0, 3]])
# print(my_csv_df.loc[my_csv_df['Age'] > 30])
# print(my_csv_df.loc[(my_csv_df['Age'] > 30) & (my_csv_df['Age'] < 40)])

# Ensure the second row contains numeric data
# numeric_cols = my_csv_df.select_dtypes(include=[np.number]).columns
# print(my_csv_df.loc[:, my_csv_df.loc[1, numeric_cols] > 30])
# print(my_csv_df.loc[:, my_csv_df.iloc[:, 1] > 30])

# Ensure the second column contains numeric data
numeric_cols = my_csv_df.select_dtypes(include=[np.number]).columns

# Create a boolean Series based on the condition applied to the second column
condition = my_csv_df.iloc[:, 1] > 30
condition2 = my_csv_df.iloc[:, 1].apply(pd.to_numeric, errors='coerce') > 30
# Use the boolean Series to filter rows
filtered_df = my_csv_df[condition]
# print(filtered_df)

# print(my_csv_df.head(10))

# print(my_csv_df.tail(10))

# print(my_csv_df.info())
# print(my_csv_df['City'])
print(my_csv_df.City)
print(my_csv_df.iloc[:, 2])
# print(my_csv_df['City'].value_counts())
# print(my_csv_df['City'].unique())
# print (my_csv_df['City'].nunique())
# print(my_csv_df['City'].apply(len))
# print(my_csv_df['City'].apply(lambda x: x.upper()))
# print(my_csv_df.drop('City', axis=1, inplace=True))


