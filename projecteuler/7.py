def primes(n):
    primes = [2,3]
    p=3
    while p <= n:
        for i in primes:
            if p % i == 0:
                break
        else:
            primes.append(p)
        p += 2
    return primes

ps = primes(1000000)
print(ps)
print(len(ps))
print(ps[10000])
print(ps[10001])