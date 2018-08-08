# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 01:55:44 2017

@author: whisp
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('bmh')
matplotlib.rcParams['figure.figsize']=(10,10)

# X
X = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
y = np.array([1,1,-1,-1])

# 邊界
x_min, y_min = X.min(axis=0)-1
x_max, y_max = X.max(axis=0)+1

# 座標點
grid  = np.mgrid[x_min-1:x_max+1:200j, y_min-1:y_max+1:200j]
# grid.shape = (2, 200, 200)

from mpl_toolkits.mplot3d import Axes3D
ax = plt.gca(projection='3d')
ax.plot_surface(grid[0], grid[1], 0.5, cmap=plt.cm.rainbow, alpha=0.2)
#ax.plot_wireframe(grid[0], grid[1], Z, alpha=0.2, rstride=20, cstride=20)
ax.scatter(X[:, 0], X[:, 1], y, c=y, cmap=plt.cm.rainbow, s=30);
ax.set_zlim3d(-2,2)
ax.set_xlim3d(-3,3)
ax.set_ylim3d(-3,3)
ax.view_init(15, 75)
plt.savefig('VC-dimension.png', dpi=1200)





