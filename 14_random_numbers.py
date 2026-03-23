import numpy as np

rng = np.random.default_rng()

print(rng.integers(low=1,high=7))
#7 in not included

print(rng.integers(low=1,high=101,size=3))
#gives 3 numbers

print(rng.integers(low=1,high=101,size=(3,2)))
#gives 3 numbers and 3 rows that are row 0,1,2

print(np.random.uniform())
print(np.random.uniform(low=-1,high=1))

print(np.random.uniform(low=-1,high=1,size=(3,2)))

np.random.seed(seed=1)
print(np.random.uniform(low=-1,high=1,size=(3,2)))

# Without seed → shuffle randomly every time
# With seed → same shuffle order every time

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits = np.array(['apple','banana','pineapple','coconut','orange'])
rng.shuffle(fruits)
print(fruits)

fruits = rng.choice(fruits)
print(fruits)

fruits = np.array(['apple','banana','pineapple','coconut','orange'])
result = rng.choice(fruits, size=(3,2))
print(result)