def prime_factor_counts(n):
    counts = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            counts[d] = counts.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        counts[n] = counts.get(n, 0) + 1
    return counts

print(prime_factor_counts(29),prime_factor_counts(30),prime_factor_counts(31))

for i in range(10,1_000_000):
    f1 = prime_factor_counts(i)
    f2 = prime_factor_counts(i+1)
    f3 = prime_factor_counts(i+2)
    f4 = prime_factor_counts(i+3)
    if len(f1.keys()) != 4 or len(f2.keys()) != 4 or len(f3.keys()) != 4 or len(f4.keys()) != 4:
        continue
    print(i,i+1,i+2,i+3)
    break