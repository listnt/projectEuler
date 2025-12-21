import itertools

def eratosphen(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]


pD = {}
primesD = {}
primes = eratosphen(int(1e6))

for prime in primes:
    primesD[prime] = 1
    primestr = str(prime)
    for i in range(0,10):
        indexes = []
        for j in range(len(primestr)):
            c = primestr[j]
            if c==str(i):
                indexes.append(j)
        if len(indexes)<2:
            continue
        for j in range(2,len(indexes)+1):
            combinations = list(itertools.combinations(indexes,j))
            for comb in combinations:
                primestrl = list(primestr)
                for k in comb:
                    primestrl[k] = "*"
                mask = ''.join(primestrl)
                if mask not in pD:
                    pD[mask] = []
                pD[mask].append(prime)
            
for key in pD.keys():
    if len(pD[key])==8:
        print(pD[key])