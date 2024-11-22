import numpy as np #numpy - numerical python

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