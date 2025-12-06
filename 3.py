def prime_factors(n):
    largestFactor = 0
    # factor out 2s
    while n % 2 == 0:
        largestFactor = 2
        n //= 2

    p = 3
    while p * p <= n:
        while n % p == 0:
            largestFactor = p
            n //= p
        p += 2

    # remainder is prime
    if n > 1:
        largestFactor = n
    return largestFactor
N = 600851475143
print(prime_factors(N))
