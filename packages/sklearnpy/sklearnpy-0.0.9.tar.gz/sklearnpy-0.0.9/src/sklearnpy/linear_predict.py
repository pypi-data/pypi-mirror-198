# import numpy as np

# from sklearn.linear_model import LinearRegression

# print("Predict 12 inch cost:$%.2f" % (LinearRegression().fit(np.mat(list(map(int, input().split(' ')))).reshape(
#     5, 1), np.mat(list(map(float, input().split(' ')))).reshape(5, 1)).predict([[int(input())]])), end="")


def println():
    print(''' 
    (LinearRegression().fit(np.mat(list(map(int,input().split(' ')))).reshape(5,1),np.mat(list(map(float,input().split(' ')))).reshape(5,1)).predict([[int(input())]])), end="")
    
    ''')
