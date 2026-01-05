def eratosphen(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

odds = []

primes = eratosphen(1000000)
primesD = {}
for i in range(len(primes)):
    primesD[primes[i]] = i
    
i=9
while i < 1_000_000:
    i+=2
    if i in primesD:
        continue
    flag = False
    k = 1 
    while 2*k*k < i:
        if i-2*k*k in primesD:
            flag = True
            break
        k+=1
    if not flag:
        print(i)
        break