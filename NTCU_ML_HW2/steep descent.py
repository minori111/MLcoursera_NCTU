# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:09:01 2017

@author: whisp
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def grdlines(Q, x0, esp = 10**(-8)):
    Q = np.array(Q)
    x0 = np.array(x0)
    flag =1
    iter_ = 0
    x_curve = []
    x_curve.append(x0)
    while flag > esp:
        grad = Q @ x0
        temp1 = np.linalg.norm(grad)**2
        if temp1 < 10**(-12):
            flag = esp
        else:
            stepsize = temp1/(grad.T @ Q @ grad)
            x1 = x0 - stepsize*grad
            flag = np.linalg.norm(x1-x0)
            x0 = x1
            x_curve.append(x0)
        iter_ = iter_ + 1
    x = x0
    f_value = 0.5*x.T @ Q @ x
    return x, f_value, iter_, x_curve

Q = np.array([[1, 0], [0, 900]])
x0 = np.array([1000, 1])
#x0 = np.array([1, 1000])

x, f_value, iter_, x_curve = grdlines(Q, x0)
print('x: ' + str(x))
print('f_value: ' + str(f_value))
print('iter_: ' + str(iter_))
x_curve_array = np.array(x_curve).T
plt.plot(x_curve_array[0][::5], x_curve_array[1][::5])
plt.savefig('steep descent with exact line search.png', dpi=1200)

#%%

def newton(Q, x0, esp = 10**(-8)):
    Q = np.array(Q)
    x0 = np.array(x0)
    flag =1
    iter_ = 0
    x_curve = []
    x_curve.append(x0)
    while flag > esp:
        grad = Q @ x0
        temp1 = np.linalg.norm(grad)**2
        if temp1 < 10**(-12):
            flag = esp
        else:
            step = np.linalg.inv(Q) @ grad
            x1 = x0 - step
            flag = np.linalg.norm(x1-x0)
            x0 = x1
            x_curve.append(x0)
        iter_ = iter_ + 1
    x = x0
    f_value = 0.5*x.T @ Q @ x
    return x, f_value, iter_, x_curve

Q = np.array([[1, 0], [0, 900]])
x0 = np.array([1000, 1])
#x0 = np.array([1, 1000])

x, f_value, iter_, x_curve = newton(Q, x0)
print('x: ' + str(x))
print('f_value: ' + str(f_value))
print('iter_: ' + str(iter_))
x_curve_array = np.array(x_curve).T
plt.plot(x_curve_array[0][::], x_curve_array[1][::])
plt.savefig('Newton.png', dpi=1200)




