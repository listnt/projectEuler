import math
def isPentagonal(p):
    k = math.isqrt(1+24*p)
    n = (1 + k)//6
    if n*(3*n-1)//2 == p:
        return True
    return False

for i in range(1000000):
    h = i*(2*i-1)
    if isPentagonal(h):
        print(h,i)
        