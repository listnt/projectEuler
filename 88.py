import math

def unique_factorizations(n, start=2):
    result = []
    for i in range(start, n + 1):
        if n % i == 0:
            quotient = n // i
            if quotient >= i:
                result.append([i, quotient])
            for subfactor in unique_factorizations(quotient, i):
                result.append([i] + subfactor)
    return result

ns = [24_000]*(12_001)
ns[0]=0
ns[1]=0
for i in range(4,24_000):
    factors = unique_factorizations(i)
    for f in factors:
        ones = math.prod(f) - sum(f)
        k_support = ones + len(f)
        if k_support<=12_000:
            ns[k_support] = min(ns[k_support], i)
import numpy as np

ns = np.unique(ns)

print(sum(ns))