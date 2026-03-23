import numpy as np

# Element-wise arithmetic
array = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("Array 1:", array)
print("Array 2:", array2)

# Addition
print("Add:", array + array2)        # [5 7 9]

# Subtraction
print("Subtract:", array - array2)   # [-3 -3 -3]

# Multiplication
print("Multiply:", array * array2)   # [4 10 18]

# Division
print("Divide:", array / array2)     # [0.25 0.4 0.5]

# Power
print("Power:", array ** array2)     # [1^4, 2^5, 3^6]