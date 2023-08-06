

import numpy as np

try:
    a, b = np.linalg.eig(np.array([int(i)
                         for i in input().split(' ')]).reshape(5, 5))
    print(a, '\n', b)
except:
    print('输入有错！')






















































def println():
    print(''' 
    a,b = np.linalg.eig(np.array([int(i) for i in input().split(' ')]).reshape(5,5))
    ''')
