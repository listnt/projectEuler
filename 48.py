def powermod(n,p,m):
    res = 1
    while p:
        if p & 1:
            res = res * n % m
        n = n * n % m
        p >>= 1
    return res

sun = 0
for i in range(1,1001):
    sun += powermod(i,i,int(1e12))
print(sun)
