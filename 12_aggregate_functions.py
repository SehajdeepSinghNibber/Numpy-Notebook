import numpy as np

array = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))
print(np.argmax(array))

# axis = 0 → DOWN the rows (operate column-wise)
# Think: collapse rows → keep columns

print(np.sum(array, axis=0))
# [1+6, 2+7, 3+8, 4+9, 5+10]
# [7,   9,   11,  13,  15]


# axis = 1 → ACROSS the columns (operate row-wise)
# Think: collapse columns → keep rows

print(np.sum(array, axis=1))
# [1+2+3+4+5,   6+7+8+9+10]
# [15,40]