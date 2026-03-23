import numpy as np

# Create a sample 3x9 array
array = np.arange(27).reshape(3, 9)

# Array looks like:
# [[ 0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26]]

print(array[:, 1::3])  
# all rows, columns after jump of 3 starting from index 1
# picks columns: 1, 4, 7

# Output:
# [[ 1  4  7]
#  [10 13 16]
#  [19 22 25]]