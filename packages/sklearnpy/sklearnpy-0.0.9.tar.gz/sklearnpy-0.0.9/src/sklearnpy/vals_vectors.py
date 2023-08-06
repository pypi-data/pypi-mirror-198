'''
Find the eigenvalues ​​and eigenvectors of a random matrix

====

For example 

Input 25 integer data, then convert it into a 5X5 matrix, find its eigenvalues ​​and eigenvectors, 
please refer to the sample for the correct input format, if the input format is not int or the number of inputs is wrong, 
the output: the input has wrong!



Provides
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation


How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://www.scipy.org>`_.

We recommend exploring the docstrings using
`IPython <https://ipython.org>`_, an advanced Python shell with
TAB-completion and introspection capabilities.  See below for further
instructions.


'''

# import numpy as np

# try:
#     a, b = np.linalg.eig(np.array([int(i)
#                          for i in input().split(' ')]).reshape(5, 5))
#     print(a, '\n', b)
# except:
#     print('输入有错！')


def println():
    print(''' 
    a,b = np.linalg.eig(np.array([int(i) for i in input().split(' ')]).reshape(5,5))
    ''')
