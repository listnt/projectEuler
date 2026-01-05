import math

p,q = 2,5
while q <= 1000001:
    p = 3 + p
    q = 7 + q
    if q > 1000001:
        p = p - 3
        q = q - 7
        break
    g = math.gcd(p,q)
    p = p//g
    q = q//g

print(p,q)