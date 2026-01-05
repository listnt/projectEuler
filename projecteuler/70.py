def eratosphen(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def isPermutation(s1,s2):
    return sorted(str(s1)) == sorted(str(s2))


minp0 = 100000
minp1 = 100000
minP = 100000
primes = eratosphen(10000)
for i,p0 in enumerate(primes):
    for p1 in primes[i:]:
        if p0*p1 > 10000000:
            break
        p = (p0-1)*(p1-1)
        if isPermutation(p0*p1,p) and (p0*p1)/p < minP:
            minP = (p0*p1)/p
            minp0=p0
            minp1=p1
print(minp0*minp1)

