import numpy as np

# vectorized arithmetic
array = np.array([1, 2, 3])

print("Original:", array)

print("sqrt:", np.sqrt(array))     # square root
print("floor:", np.floor(np.sqrt(array)))   # floor (round down)

# More common vectorized operations:

print("ceil:", np.ceil(array))     # round up
print("exp:", np.exp(array))       # e^x
print("log:", np.log(array))       # natural log
print("abs:", np.abs(array))       # absolute value

# Trigonometric
print("sin:", np.sin(array))
print("cos:", np.cos(array))
print("tan:", np.tan(array))

print(np.pi)

radii=np.array([1,2,3])

print(np.pi*radii**2)