import math

odds = 0
for i in range(2,10001):
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
    if (len(triplets)-1) % 2==1:
        odds+=1
print(odds)