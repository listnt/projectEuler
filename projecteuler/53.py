def binom(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)  # symmetry
    c = 1
    for i in range(1, k + 1):
        c = c * (n - k + i) // i
    return c

sun =0 
for i in range(1,101):
    for j in range(1,i+1):
        if binom(i,j)>1000000:
            sun += 1
print(sun)