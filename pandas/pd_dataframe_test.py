import pandas as pd, numpy as np
from numpy.random import randn
import os

"""
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

print(my_csv_df.loc[2])
"""


# my_df_dogs = pd.read_csv('C:/Users/BS01395/Documents/GitHub/py_learn/pandas/dog_data_2000.csv')
my_df_dogs = pd.read_csv('pandas/dog_data_2000.csv')
# print(my_df_dogs)


# Construct the relative path
file_path = os.path.join(os.path.dirname(__file__), 'dog_data_2000.csv')
my_df_dogs = pd.read_csv(file_path)
# print(f'CSV Path = {file_path}')
# print(f'File Path = {os.path.dirname(__file__)}')
# print(f'CSV File Path = {os.path.dirname('dog_data_2000.csv')}')
# print(my_df_dogs)

# print(my_df_dogs['Color'].value_counts())
# print(my_df_dogs['Color'].unique())
# print(my_df_dogs['Breed'].value_counts(dropna=False))
# print(my_df_dogs['Color'].value_counts(normalize=True))
# print((my_df_dogs['Color'].value_counts(normalize=True) * 100).round(3))
# print(my_df_dogs['Color'].value_counts(normalize=True).apply(lambda x: x * 100))
# print(my_df_dogs['Color'].value_counts(normalize=True).apply(lambda x: x * 100).round(3))
# print(my_df_dogs['Color'].value_counts(normalize=True).apply(lambda x: x * 100).round(3).sort_index())
# print(my_df_dogs['Color'].value_counts(normalize=True).apply(lambda x: x * 100).round(3).sort_values())
# print(my_df_dogs['Color'].value_counts()['Black'])
# print(my_df_dogs.groupby('Color').size().sort_values(ascending=False))
# print(my_df_dogs.groupby('Color').count())


#add column from list
Breed = ['Labrador', 'Poodle', 'Husky', 'Poodle', 'Labrador']
Color = ['Black', 'White', 'Brown', 'White', 'Black']
DogName = ['Buddy', 'Daisy', 'Rex', 'Lucky', 'Bella']
Owner = ['John', 'Jane', 'Bob', 'Alice', 'Eve']
gender = ['Male', 'Female', 'Male', 'Male', 'Female']
my_df_dogs_list = pd.DataFrame(Breed, Color, DogName, Owner)
print(my_df_dogs_list)