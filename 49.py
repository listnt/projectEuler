def eratosphen(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def isPermutation(a,b):
    return sorted(str(a)) == sorted(str(b))


primes = eratosphen(10000)
primes = [i for i in primes if len(str(i)) == 4]

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if isPermutation(primes[i],primes[j]):
            for k in range(j+1, len(primes)):
                if isPermutation(primes[j],primes[k]):
                    if abs(primes[k]-primes[j]) == abs(primes[j]-primes[i]):
                        print(primes[i],primes[j],primes[k])