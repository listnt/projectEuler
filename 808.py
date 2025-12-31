import math

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse(n):
    return int(str(n)[::-1])

def eratosphen(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

primes = eratosphen(50000000)

j=0
total =0
for p in primes:
    n = p*p
    n=reverse(n)
    if isPalindrome(n):
        continue
    s= math.isqrt(n)
    if s*s != n:
        continue
    if isPrime(s):
        j+=1
        total+=(p*p+s*s)/2
        print(s,p)
    if j==50:
        break
print(total)