import numpy as np, pandas as pd

# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x) # Output: b'1' b'2' b'3'
 

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for y in np.nditer(arr2[:, ::2]):
  print(y)
  
# for idx, z in np.ndenumerate(arr2):
#   print(idx, z)
  
# for idx, a in np.ndenumerate(arr2):
#   print(idx, a)
  
# arr3 = np.array([1, 2, 3, 4])
# print(arr3.dtype)

# my_set = {10, 3, 5, 1, 7, 2, 8, 4, 6, 9}
# print(my_set)  # Output order may vary

# #array search
# arr_search = np.array([[1, 2, 3, 4, 5, 4, 4], [1, 2, 3, 4, 5, 64, 7], [1, 2, 3, 4, 5, 8, 9]])   
# find_x = np.where(arr_search == 4)
# print("Indices where element is 4:", find_x)

# odd_num = np.where(arr_search % 2 == 1)
# print("Indices where element is odd:", odd_num)


# arr4 = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr4, 7)
# print(x)

# arr5 = np.array([1, 3, 5, 7])
# indices = np.searchsorted(arr5, [2, 4, 6])
# print(indices)  # Output: [1, 2, 3]

# # Original sorted array
# arr6 = np.array([1, 3, 5, 7])
# # Values to be inserted
# values_to_insert = [2, 4, 6]
# # Find indices where values should be inserted
# indices = np.searchsorted(arr6, values_to_insert)
# print(indices)  # Output: [1 2 3]
# # Insert values at the specified indices
# arr_sorted = np.insert(arr6, indices, values_to_insert)
# print(arr_sorted)  # Output: [1 2 3 4 5 6 7]

# arr7 = np.array([7, 50, 11, 8])
# arr7_sorted = np.sort(arr7)
# arr_sort_right = np.searchsorted(arr7_sorted, [10, 2, 9], side='right')
# print(arr_sort_right)  # Output: [2 0 3]
# print(np.insert(arr7_sorted, arr_sort_right, [10, 2, 9]))  # Output: [ 2  7  8  9 10 11 50]

# arr_sort_left = np.searchsorted(arr7_sorted, [10, 2, 9], side='left')
# print(arr_sort_left)  # Output: [2 0 3]
# print(np.insert(arr7_sorted, arr_sort_left, [10, 2, 9]))  # Output: [ 2  7  8  9 10 11 50]

# # arr8 = np.array([6, 7, 8, 9])
# # x = np.searchsorted(arr8, 7, side='right')
# # print(x)

arr_check = np.array([41, 42, 43, 44])

x = arr_check[[True, False, True, False]]
print(x)

chek = [ True, False, False, False]
newarr = arr_check[chek]
print (newarr)

filter_arr = []
for element in arr_check:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
new_filter_arr = arr_check[filter_arr]
print(new_filter_arr)