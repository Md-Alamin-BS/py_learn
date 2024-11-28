import numpy as np  

np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])  # Create a 1-D numpy array
# print(np1.shape) # Output: (12,) - 1-D array with 12 elements

# np2 = np1.reshape(2,6) # Reshape the numpy array
# print(np2)
# print(np2.shape) # Output: (2, 6) - 2-D array with 2 rows and 6 columns

np3 = np1.reshape(3,2,2) # Reshape the numpy array
print(np3)
print(np3.shape) # Output: (3, 2, 2) - 3-D array with 3 blocks, 2 rows, and 2 columns
np5 = np1.reshape(2,2,3) # Reshape the numpy array
print(np5)
print(np5.shape) # Output: (2, 2, 3) - 3-D array with 2 blocks, 2 rows, and 3 columns

# np4 = np1.reshape(-1) # Reshape the numpy array to 1-D array
# print(np4)
# print(np4.shape) # Output: (12,) - 1-D array with 12 elements

