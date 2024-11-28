import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9,10])

np2 = np1.view() # Create a view of the numpy array

print(f'Orginal NP1 {np1}')
print(f'Orginal NP2 {np2}')

np1[0] = 100 # Modify the original numpy array

print(f'NP1 after modification in NP1: {np1}')
print(f'NP2 after modification in NP2: {np2}')

np2[1] = 200 # Modify the view of the numpy array

print(f'NP1 after modification in NP2: {np1}')
print(f'NP2 after modification in NP2: {np2}')

np3 = ([1,2,3,4,5,6,7,8,9,10])
np4 = np3.copy() # Create a copy of the numpy array
print(f'Orginal NP3 {np3}')
print(f'Orginal NP4 {np4}')

np3[0] = 100 # Modify the original numpy array

print(f'NP3 after modification in NP3: {np3}')  
print(f'NP4 after modification in NP3: {np4}')

np4[1] = 200 # Modify the copy of the numpy array

print(f'NP3 after modification in NP4: {np3}')
print(f'NP4 after modification in NP4: {np4}')