import numpy as np

array = np.array('A')

print(array.ndim)

array_1 = np.array([['A','B','C'],
                    ['D','E','F'],
                    ['G','H','I']])

print(array_1.ndim)

array_1 = np.array([[
    ['A','B','C'],
    ['D','E','F'], 
    ['G','H','I']
    ],
    [
        ['J','K','L'],
        ['M','N','O'],
        ['P','Q','R']
        ],
        [
            ['S','T','U'],
            ['V','W','X'],
            ['Y','Z',' ']
            ]])

print(array_1.ndim)