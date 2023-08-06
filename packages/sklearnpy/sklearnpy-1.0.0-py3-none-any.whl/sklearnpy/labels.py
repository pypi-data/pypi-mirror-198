import numpy as np

from sklearn.cluster import AgglomerativeClustering

arr = np.array([float(i) for i in input().split(' ')]).reshape(
    *[int(i) for i in input().split(' ')])

res = AgglomerativeClustering(int(input())).fit(arr.T).labels_
print("香气和酸质{val}属于一类。".format(val='' if res[0] == res[2] else '不'), end='')






























def println():
    print(''' arr = np.array([float(i) for i in input().split(' ')]).reshape(*[int(i) for i in input().split(' ')])
res = AgglomerativeClustering(int(input())).fit(arr.T).labels_
("".format(val = '' if res[0]==res[2] else '不'),end='')''')
