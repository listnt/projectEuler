import collections

def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return collections.Counter(factors)

def phi(factors):
    p=1
    for f in factors.keys():
        p*=f**(factors[f]-1)*(f-1)
    return p

maxP = 0
for i in range(2,1000001):
    fs = prime_factorization(i)
    p = phi(fs)
    if i/p > maxP:
        maxP = i/p
        print(i,maxP)