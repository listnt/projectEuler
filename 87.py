def eratosphen(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def intpow(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return intpow(x * x, y // 2)
    else:
        return x * intpow(x * x, (y - 1) // 2)

primes = eratosphen(10_000)

mem={}
n=0
for i in range(len(primes)):
    for j in range(len(primes)):
        for k in range(len(primes)):
            if primes[i]**2+ primes[j]**3+primes[k]**4 > 50_000_000:
                break
            if primes[i]**2 + primes[j]**3 + primes[k]**4 < 50_000_000:
                mem[intpow(primes[i],2)+intpow(primes[j],3)+intpow(primes[k],4)]=1
        if primes[i]**2 + primes[j]**3 > 50_000_000:
            break
print(len(mem))