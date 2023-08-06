import numpy as np
from sklearn.cluster import KMeans


arr = np.array([float(i) for i in input().split(' ')]).reshape(
    *[int(i) for i in input().split(' ')])
kmeans = KMeans(n_clusters=int(input())).fit(arr)
print('A公司所在类的中心为：{:.2f},{:.2f}。'.format(kmeans.cluster_centers_[
      kmeans.labels_[0], 0], kmeans.cluster_centers_[kmeans.labels_[0], 1]), end='')




































def println():
    print(''' 
    arr = np.array([float(i) for i in input().split(' ')]).reshape(
    *[int(i) for i in input().split(' ')])
kmeans = KMeans(n_clusters=int(input())).fit(arr)
(''.format(kmeans.cluster_centers_[
      kmeans.labels_[0], 0], kmeans.cluster_centers_[kmeans.labels_[0], 1]), end='')
    
    ''')
