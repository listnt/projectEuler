def nCk(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)  # symmetry
    c = 1
    for i in range(1, k + 1):
        c = c * (n - k + i) // i
    return c


print(nCk(40,20))