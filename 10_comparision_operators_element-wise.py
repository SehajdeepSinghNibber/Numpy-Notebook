import numpy as np

array = np.array([1, 2, 3])
array2 = np.array([2, 2, 2])

print("Array 1:", array)
print("Array 2:", array2)

# Element-wise comparisons
print("Equal:", array == array2)        # [False True False]
print("Not Equal:", array != array2)   # [True False True]
print("Greater than:", array > array2) # [False False True]
print("Less than:", array < array2)    # [True False False]
print("Greater or equal:", array >= array2) # [False True True]
print("Less or equal:", array <= array2)    # [True True False]