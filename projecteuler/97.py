p = 7830457
a = 28433

mod = int(10**10)

n=2

for i in range(1,p):
    n = n*2 % mod
print((a*n+1)%mod)