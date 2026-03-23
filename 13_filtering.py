import numpy as np

arr = np.array([[10, 25, 30, 45],
                [50, 65, 70, 85]])

# elements > 40
print(arr[arr > 40])
# [45 50 65 70 85]

# indices where condition is true (row indices, col indices)
print(np.where(arr > 40))
# (array([0,1,1,1,1]), array([3,0,1,2,3]))

# replace >40 with 100, else keep original
print(np.where(arr > 40, 100, arr))
# [[10 25 30 100]
#  [100 100 100 100]]

# elements between 30 and 70
print(arr[(arr > 30) & (arr < 70)])
# [45 50 65]

# elements divisible by 5 AND > 30
print(arr[(arr % 5 == 0) & (arr > 30)])
# [45 50 65 70 85]

# rows where row sum > 150
print(arr[arr.sum(axis=1) > 150])
# [[50 65 70 85]]

# columns where column mean > 40
print(arr[:, arr.mean(axis=0) > 40])
# [[50 65 70 85] column-wise filter → keeps last 4 columns]

# replace values < 50 with 0
arr2 = arr.copy()
arr2[arr2 < 50] = 0
print(arr2)
# [[0 0 0 0]
#  [50 65 70 85]]

# keep only values present in given list
print(arr[np.isin(arr, [25, 70, 85])])
# [25 70 85]

# pick specific elements (0,2) and (1,3)
print(arr[[0, 1], [2, 3]])
# [30 85]

# replace values between 30–70 with -1
print(np.where((arr > 30) & (arr < 70), -1, arr))
# [[10 25 30 -1]
#  [-1 -1 70 85]]