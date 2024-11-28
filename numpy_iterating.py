import numpy as np

# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)
 
  
# arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for y in np.nditer(arr2[:, ::2]):
#   print(y)
  
# for idx, z in np.ndenumerate(arr):
#   print(idx, z)
  
# for idx, a in np.ndenumerate(arr2):
#   print(idx, a)
  
# arr = np.array([1, 2, 3, 4])
# print(arr.dtype)

my_set = {10, 3, 5, 1, 7, 2, 8, 4, 6, 9}
print(my_set)  # Output order may vary

#array search
arr_search = np.array([[1, 2, 3, 4, 5, 4, 4], [1, 2, 3, 4, 5, 64, 7], [1, 2, 3, 4, 5, 8, 9]])   
find_x = np.where(arr_search == 4)
print("Indices where element is 4:", find_x)

odd_num = np.where(arr_search % 2 == 1)
print("Indices where element is odd:", odd_num)
