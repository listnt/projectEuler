def divisors(n):
    k=0
    for i in range(1, n):
        if n % i == 0:
            k+=1
    return k+1

t=28
for i in range(8,1000000):
    t+=i
    if i < 4000:
        continue
    divs = divisors(t)
    print(i,t,divs)
    if divs > 500:
        print(t)
        break