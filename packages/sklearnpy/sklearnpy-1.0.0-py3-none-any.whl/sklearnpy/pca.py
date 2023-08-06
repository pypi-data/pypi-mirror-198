
import numpy as np

arr = np.array([float(i) for i in input().split(',')]).reshape(*[int(i) for i in input().split(',')])
u,v = np.linalg.eig(np.cov(((arr-np.mean(arr))/np.std(arr)).T))
index = 0 if u[0]>u[1] else 1
print('第1主成分={:.5f}*(x1-{:.2f}){:+.5f}*(x2-{:.2f})'.format(v[0][index],np.mean(arr,axis=0)[0],v[1][index],np.mean(arr,axis=0)[1]),end='')










































def println():
    print(''' arr = np.array([float(i) for i in input().split(',')]).reshape(*[int(i) for i in input().split(',')])
u,v = np.linalg.eig(np.cov(((arr-np.mean(arr))/np.std(arr)).T))
index = 0 if u[0]>u[1] else 1
(''.format(v[0][index],np.mean(arr,axis=0)[0],v[1][index],np.mean(arr,axis=0)[1]),end='')''')