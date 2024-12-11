import numpy as np #numpy - numerical python
# from numpy import random

'''
np1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
print(np1)

np1 = np1.reshape(6,2)
print(np1)

np2=np.arange(0,10,2)
print(f"Arange array {' '.join(map(str, np2))}")
print(f"Shape of np2: {np2.shape}")

np3=np.zeros((3,3))
print(np3)

np4=np.ones((3,3))
print(np4)

np6=np.full((3), 1)
print(np6)

np7=np.full((3,3), 10)   # 3x3 matrix with all elements as 10
print(np7)

list = [1,2,3,4,5,6,7,8,9]
np8 = np.array(list)
print(np8)

# Slicing numpy array
np9 = np1[1:5]
print(np9)

np10= np.array([1,2,3,4,5,6,7,8,9])
print(np10[4:])
print(np10[-6:-1])


# Print the array in reverse order
print(np10[::-1])

# Specify start and end indices for backward print
start = -6  # Start from the 6th element from the end
end = -1    # End at the element before the last one

# Print the specified slice in reverse order
print(np10[start:end][::-1])

print(np10[-1:-9:-1])


# Steps
np11=np.arange(0, 101, 5) 
print(np11)


np2 = np1.reshape(6,2) # Reshape the numpy array
# print(np2)


arr = np.array([
[1, 2, 3], 
[4, 5, 6],
[7, 8, 9],
[10, 11, 12],
[13, 14, None] # None and zero(0) can be used as placeholder for missing values. Array requires same number of elements in each row/2 dimentional array
])
newarr = arr.reshape(-1)
# print(newarr)

arr2 = np.array([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14]
], dtype=object)
newarr2 = np.concatenate(arr2)
print(newarr2)

arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])
arr = np.stack((arr3, arr4))
print(arr)

print(f"Exponential of 2: {np.exp(2)}") # Exponential of 2 is 7.38905609893065

# Using enumerate to get index and value
my_list = [1, 2, 3, 4, 5]
for index, value in enumerate(my_list): # Enumerate returns both index and value separately in two variables from my_list
    if index % 2 == 0:  # Custom condition: only print values at even indices
        print(value)
        

arr_rearrange = np.array([1, 2, 3, 4, 5])
print(np.random.permutation(arr_rearrange))  # Output: [1 2 4 5 3] or different every time, does not change the original array

np.random.shuffle(arr_rearrange) # Output: [5 2 1 3 4] or different every time, changes the original array
print(arr_rearrange)

'''

np_search = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2])

x = np.where(np_search == 2) # Output: (array([1, 11], dtype=int64),)
# print(np_search)
print(x)
print(x[0]) # Output: [1 11]
print(x[0][0]) # Output: 1
print(np_search[x[0]]) # Output: [2 2]
