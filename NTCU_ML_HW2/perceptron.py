# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 05:02:24 2017

@author: whisp
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('bmh')
# Make a prediction with weights
def predict(Xi, weights, bias):
	activation = (weights.T @ Xi) + bias
	return 1.0 if activation >= 0.0 else -1.0

def train_weights(X, y, l_rate = 0.1, n_epoch = 10):
    R = max([xi.T @ xi for xi in X])
    bias = 0.0
    weights = np.array([0.0 for i in range(len(X[0]))])
    for epoch in range(n_epoch):
        sum_error = 0.0
        for i in range(len(X)):
            if y[i]*((weights.T @ X[i]) + bias) <= 0:
                bias = bias + l_rate*y[i]*(R**2)
                weights = weights + l_rate*y[i]*X[i]
                #print(i, weights, bias)
        for j in range(len(X)):
            if predict(X[j], weights, bias) != y[j]:
                sum_error = sum_error + 1
        #print(weights, bias)
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return weights, bias

def perceptron_Primal(X, y, l_rate = 0.1, n_epoch = 100):
	predictions = []
	weights, bias = train_weights(X, y, l_rate, n_epoch)
	for i in range(len(X)):
		predictions.append(predict(X[i], weights, bias))
	return predictions

def gen_R4(X):
    result = []
    for i in range(len(X)):
        result.append([-X[i][0]*X[i][1], X[i][0]*X[i][0], X[i][0]*X[i][1], X[i][1]*X[i][1]])
    return np.array(result) 



   


   

def train_weights_Dual(X, y, n_epoch = 15):
    R = max([xi.T @ xi for xi in X])
    bias = 0.0
    alpha = np.array([0 for i in range(len(X))])
    for epoch in range(n_epoch):
        weights = np.array([0.0 for i in range(len(X[0]))])
        sum_error = 0
        for i in range(len(X)):
            dual_sum = 0
            for j in range(len(X)):
                dual_sum = dual_sum + alpha[j]*y[j]*((X[j] @ X[i])**2)
            #print(y[i]*(dual_sum + bias), dual_sum)
            if y[i]*(dual_sum + bias)<=0:
                alpha[i] = alpha[i]+1
                bias = bias + y[i]*R
       # print()
        for i in range(len(X)):       
            weights = weights + alpha[i]*y[i]*X[i]
        for j in range(len(X)):
            if predict(X[j], weights, bias) != y[j]:
                sum_error = sum_error + 1          
            #print((weights.T @ X[j]) + bias)
        #print(alpha, bias, sum(alpha))
        #print(list(alpha), bias)
        print('>epoch=%d, error=%.3f' % (epoch, sum_error))
    return weights, bias



def perceptron_Dual(X, y, n_epoch = 15):
	predictions = []
	weights, bias = train_weights_Dual(X, y, n_epoch);#print(weights)
	for i in range(len(X)):
		predictions.append(predict(X[i], weights, bias))
	return predictions



X = np.array([[0,0],[0.5,0],[0,0.5],[-0.5,0],[0,-0.5],
              [0.5,0.5],[0.5,-0.5],[-0.5,0.5],[-0.5,-0.5],[1,0],[0,1],[-1,0],[0,-1]])
y = np.array([1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1])    
print(perceptron_Primal(gen_R4(X), y, l_rate = 0.1, n_epoch = 15))  
weights, bias = train_weights_Dual(X, y)
print(weights, bias)
print(perceptron_Dual(X, y, n_epoch = 15))


# 邊界
x_min, y_min = X.min(axis=0)-1
x_max, y_max = X.max(axis=0)+1

# 座標點
grid  = np.mgrid[x_min-1:x_max+1:200j, y_min-1:y_max+1:200j]
# grid.shape = (2, 200, 200)


# Pro3-(a)
Z = weights @ grid.reshape(2, -1) + bias
Z  = Z.reshape(grid.shape[1:])

plt.scatter(X[:,0], X[:, 1],  c=y, cmap=plt.cm.rainbow, zorder=10, s=50)
xx = np.random.uniform(-2.7,2.7,size=(2,2000))
y_ = weights @ xx + bias
plt.scatter(xx.T[:,0], xx.T[:,1],  c = y_>0, cmap=plt.cm.rainbow, zorder=10, s=10, alpha=0.5)
plt.pcolormesh(grid[0], grid[1], Z>0 , cmap=plt.cm.rainbow, alpha=0.1)
plt.contour(grid[0], grid[1], Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
                levels=[-1, 0, 1])
plt.savefig('Pro3-(a)-clf.png', dpi=1200)




# Pro3-(d)
weights, bias = train_weights(gen_R4(X), y)
G = grid.reshape(2, -1)
G = np.concatenate([(-G[0]*G[1])[:, None], (G[0]*G[0])[:, None], (G[0]*G[1])[:, None], (G[1]*G[1])[:, None]], axis=1)
Z = weights @ G.T + bias
Z  = Z.reshape(grid.shape[1:])

#3D
from mpl_toolkits.mplot3d import Axes3D
ax = plt.gca(projection='3d')
ax.plot_surface(grid[0], grid[1], Z, cmap=plt.cm.rainbow, alpha=0.2)
#ax.plot_wireframe(grid[0], grid[1], Z, alpha=0.2, rstride=20, cstride=20)
ax.scatter(X[:, 0], X[:, 1], y, c=y, cmap=plt.cm.rainbow, s=30)
plt.savefig('Pro3-(d)-3D.png', dpi=1200)  

#2D  
plt.figure()
plt.scatter(X[:,0], X[:, 1],  c=y, cmap=plt.cm.rainbow, zorder=10, s=50)
xx = np.random.uniform(-2.7,2.7,size=(2,2000)) 
xx_after = np.concatenate([(-xx[0]*xx[1])[:, None], (xx[0]*xx[0])[:, None], (xx[0]*xx[1])[:, None], (xx[1]*xx[1])[:, None]], axis=1)
y_after = weights @ xx_after.T +bias
Z = weights @ G.T + bias
Z  = Z.reshape(grid.shape[1:])
plt.scatter(xx.T[:,0], xx.T[:,1],  c = y_after>0, cmap=plt.cm.rainbow, zorder=10, s=10, alpha=0.5)
plt.pcolormesh(grid[0], grid[1], Z>0 , cmap=plt.cm.rainbow, alpha=0.1)
plt.contour(grid[0], grid[1], Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
                levels=[-1, 0, 1]) 
plt.savefig('Pro3-(d)-2D.png', dpi=1200)     
    
    
# Pro3-(c)
X = np.array([[0.5,0],[0,0.5],[-0.5,0],[0,-0.5],
              [0.5,0.5],[0.5,-0.5],[-0.5,0.5],[-0.5,-0.5]])
y = np.array([1,1,1,1,-1,-1,-1,-1])    
weights, bias = train_weights_Dual(X, y)

# 邊界
x_min, y_min = X.min(axis=0)-1
x_max, y_max = X.max(axis=0)+1

# 座標點
grid  = np.mgrid[x_min-1:x_max+1:200j, y_min-1:y_max+1:200j]
# grid.shape = (2, 200, 200)

Z = weights @ grid.reshape(2, -1) + bias
Z  = Z.reshape(grid.shape[1:])
plt.figure()
plt.scatter(X[:,0], X[:, 1],  c=y, cmap=plt.cm.rainbow, zorder=10, s=50)
xx = np.random.uniform(-2.7,2.7,size=(2,2000))
y_ = weights @ xx + bias
plt.scatter(xx.T[:,0], xx.T[:,1],  c = y_>0, cmap=plt.cm.rainbow, zorder=10, s=10, alpha=0.5)
plt.pcolormesh(grid[0], grid[1], Z>0 , cmap=plt.cm.rainbow, alpha=0.1)
plt.contour(grid[0], grid[1], Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
                levels=[-1, 0, 1])
plt.savefig('Pro3-(c)-clf.png', dpi=1200)    
