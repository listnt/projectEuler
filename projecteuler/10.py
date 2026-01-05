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

ps = primes(2000000)
print(sum(ps))