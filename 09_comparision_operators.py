import numpy as np

scores = np.array([10, 15, 31, 19, 20, 30])

print("scores:", scores)

# Comparisons with scalar
print("== 20:", scores == 20)   # [False  True False]
print("!= 20:", scores != 20)   # [ True False  True]
print("> 20:", scores > 20)     # [False False  True]
print("< 20:", scores < 20)     # [ True False False]
print(">= 20:", scores >= 20)   # [False  True  True]
print("<= 20:", scores <= 20)   # [ True  True False]

print(scores[scores >= 20])
scores[scores>=20]=0
print(scores)