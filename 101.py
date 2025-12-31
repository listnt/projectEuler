def intpow(n,p):
    res = 1
    for i in range(p):
        res *= n
    return res

def un(n):
    return 1-n+intpow(n,2)-intpow(n,3)+intpow(n,4)-intpow(n,5)+intpow(n,6)-intpow(n,7)+intpow(n,8)-intpow(n,9)+intpow(n,10)

from scipy.interpolate import lagrange
import numpy as np


total = 0
points = np.array([])
for i in range(1,11):
    points = np.append(points,i)
    y = un(points)
    
    poly = lagrange(points,y)
    fit = poly(i+1)
    total+=fit
print(total)