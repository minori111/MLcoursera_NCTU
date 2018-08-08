# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 13:25:52 2017

@author: whisp
"""

import numpy as np
from scipy import stats

A = np.array([84, 88, 76, 86, 85, 90, 72, 87, 77, 82,])
B = np.array([72, 84, 82, 80, 81, 80, 75, 86, 75, 78,])

print('Mean of A is: ' + str(np.mean(A)))
print('Standard deviation of A is: ' + str(np.std(A)))
print('Mean of B is: ' + str(np.mean(B)))
print('Standard deviation of B is: ' + str(np.std(B)))

print('Mean of A-B is: ' + str(np.mean(A-B)))
print('Standard deviation of A-B is: ' + str(np.std(A-B)))


tt = np.mean(A-B)/np.sqrt(np.var(A-B)/float(len(A)))  # t-statistic for mean
pval = stats.t.sf(np.abs(tt), len(A)-1)*2  # two-sided pvalue = Prob(abs(t)>tt)
print('t-statistic = %6.3f pvalue = %6.4f' % (tt, pval))