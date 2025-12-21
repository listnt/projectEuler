import itertools
def eratosphen(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = eratosphen(10000)
primesD = {}
for i in range(len(primes)):
    primesD[str(primes[i])] = i

def isCombInPrimes(selected,p):
    for i in selected:
        perm1 = str(i)+str(p)
        perm2 = str(p)+str(i)
        if not isPrime(int(perm1)) or not isPrime(int(perm2)):
            return False
    return True

selected = []
for p1 in primes:
    selected.append(p1)
    for p2 in primes[primesD[str(p1)]+1:]:
        if p2 in selected:
            continue
        if not isCombInPrimes(selected,p2):
            continue
        selected.append(p2)
        for p3 in primes[primesD[str(p2)]+1:]:
            if p3 in selected:
                continue
            if not isCombInPrimes(selected,p3):
                continue
            selected.append(p3)
            for p4 in primes[primesD[str(p3)]+1:]:
                if p4 in selected:
                    continue
                if not isCombInPrimes(selected,p4):
                    continue
                selected.append(p4)
                for p5 in primes[primesD[str(p4)]+1:]:
                    if p5 in selected:
                        continue
                    if not isCombInPrimes(selected,p5):
                        continue
                    print(p1,p2,p3,p4,p5, p1+p2+p3+p4+p5)
                    exit()
                selected.remove(p4)
            selected.remove(p3)
        selected.remove(p2)
    selected.remove(p1)