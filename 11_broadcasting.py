import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1*array2)

#Broadcasting happens here:
# array1 (1,4) is stretched vertically → becomes (4,4)
# array2 (4,1) is stretched horizontally → becomes (4,4)
# Then element-wise multiplication is done

# array3 = np.array([[1, 2, 3, 4],
#                    [1, 2, 3, 4],
#                    [1, 2, 3, 4],
#                    [1, 2, 3, 4]])
# array4 = np.array([[1,2],[2,3],[3,4],[4,5]])

# print(array3.shape)
# print(array4.shape)

# print(array4*array3)

# Broadcasting only works if:

# Dimensions are equal
# OR one of them is 1

array5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array6 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array5.shape)
print(array6.shape)

print(array6*array5)