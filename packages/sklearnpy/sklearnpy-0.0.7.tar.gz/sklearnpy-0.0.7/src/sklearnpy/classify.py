from numpy import *
import numpy as np
import math


def fun():
    x1 = array([float(i) for i in input().split(',')])
    y1 = array([float(i) for i in input().split(',')])
    w1 = mat(vstack((x1, y1)))
    x2 = array([float(i) for i in input().split(',')])
    y2 = array([float(i) for i in input().split(',')])
    w2 = mat(vstack((x2, y2)))
    mean1 = np.mean(w1, 1)
    mean2 = np.mean(w2, 1)
    dimens1, nums1 = w1.shape[:2]
    samples_mean1 = w1 - mean1
    s_in1 = 0
    for i in range(nums1):
        x = samples_mean1[:, i]
        s_in1 += dot(x, x.T)
    dimens2, nums2 = w2.shape[:2]
    samples_mean2 = w2 - mean2
    s_in2 = 0
    for i in range(nums2):
        x = samples_mean2[:, i]
        s_in2 += dot(x, x.T)
    s = s_in1 + s_in2
    s_t = s.I
    w = dot(s_t, mean1 - mean2)
    w_new = w.T
    m1_new = dot(w_new, mean1)
    m2_new = dot(w_new, mean2)
    pw1 = 0.6
    pw2 = 0.4
    w0 = m1_new*pw1+m2_new*pw2
    x = mat(array([float(i) for i in input().split(',')]).reshape(2, 1))
    y_i = w_new * x[:, 0]
    if y_i > w0:
        print('该点属于第一类')
    else:
        print('该点属于第二类')


# fun()
