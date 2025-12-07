def sieve(n):
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

primes = sieve(10000)

for n in range(80):
    print(n**2-61*n+971)

a=-1000
b=-1000
max_cons = 0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        cons = 0 
        for n in range(0,1000):
            if n**2 + a*n + b not in primes:
                break
            else:
                cons += 1
                
        if cons > max_cons:
            max_cons = cons
            print(a,b,max_cons)