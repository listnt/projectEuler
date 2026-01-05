def eratosphen(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]


primes = eratosphen(1000000)
primesD = {}
for i in range(len(primes)):
    primesD[primes[i]] = i
    
maxWindowSize = 1000
while sum(primes[:maxWindowSize]) > 1_000_000:
    maxWindowSize += -1
# print(maxWindowSize,sum(primes[:maxWindowSize]))

for windowSize in range(maxWindowSize, 1, -1): 
    for i in range(len(primes) - windowSize + 1):
        window = sum(primes[i:i+windowSize])
        if window in primesD:
            print(window,windowSize) 
            exit()