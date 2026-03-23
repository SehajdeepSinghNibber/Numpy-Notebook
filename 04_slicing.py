import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array[start:end:step]

print(array[0:3])

print(array[1:2])

print(array[1:4])

print(array[1:4:2])

print(array[::-1])
# reverses the list

print(array[::-1])   # reverse rows
print(array[::-2])   # reverse rows, take every 2nd row
print(array[::-3])   # reverse rows, take every 3rd row
print(array[::-4])   # reverse rows, take every 4th row

print(array[:,0])    # all rows, column 0
print(array[:,1])    # all rows, column 1
print(array[:,2])    # all rows, column 2
print(array[:,3])    # all rows, column 3

print(array[:,0:3])  # all rows, columns 0 to 2
print(array[:,2:3])  # all rows, only column 2 (2D result)
print(array[:,3:3])  # empty array (start == end)

print(array[:,1::3]) # all rows, column after jump of 3

# array = [[ 0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26]]
# print(array[:,1::3]) 
# [[ 1  4  7]
#  [10 13 16]
#  [19 22 25]]

print(array[0:3,])  # all column, rows 0 to 2

print(array[0:2,:]) # all rows, column after jump of 3
