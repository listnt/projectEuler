sun=0
for n in range(2,1000000):
    res=0
    for c in str(n):
        res+=int(c)**5
    if res==n:
        print(n)
        sun+=n
        
print(sun)