import math
import fractions

def seq(n,triplets):
    return triplets[1:][(n-1)%(len(triplets)-1)][0]

def approx(n,triplets):
    if (len(triplets)-1)%2==0:
        n=n-1
    else:
        n=2*n-1
    term = seq(n,triplets)
    frac = fractions.Fraction(1,seq(n,triplets))
    for i in range(n-1,0,-1):
        term = seq(i,triplets)
        frac = fractions.Fraction(1,term +frac)
    frac = frac + triplets[0][0]
    return frac

maxX = 0
maxP = 0

for i in range(2,1001):
    m=0
    d=1
    a0=math.isqrt(i)
    if a0*a0==i:
        continue
    a=a0
    triplets = [(a0,d,m)]
    while True:
        m = d*a - m
        d = (i-m*m)//d
        a = (a0 + m)//d
        
        if (a,d,m) in triplets:
            break
        triplets.append((a,d,m))
        
    sol = approx(len(triplets)-1,triplets)
    if sol.numerator > maxX:
        maxP = i
        maxX = sol.numerator
print(maxP)