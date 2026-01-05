from sympy import primefactors
l = [1, 0]
for n in range(2, 101):
    l.append(sum(sum(primefactors(k)) * l[n - k] for k in range(1, n + 1)) // n)
    if l[-1]>5000:
        print(n)
        break