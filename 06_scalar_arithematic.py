import numpy as np

# scalar arithmetic
array = np.array([1, 2, 3])

print("Original:", array)

# Addition
print("Add 1:", array + 1)        # [2 3 4]

# Subtraction
print("Subtract 1:", array - 1)   # [0 1 2]

# Multiplication
print("Multiply by 2:", array * 2)  # [2 4 6]

# Division
print("Divide by 2:", array / 2)    # [0.5 1.  1.5]

# Floor Division
print("Floor divide by 2:", array // 2)  # [0 1 1]

# Modulus (remainder)
print("Modulus 2:", array % 2)     # [1 0 1]

# Power
print("Power 2:", array ** 2)      # [1 4 9]