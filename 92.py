n=0
for i in range(2,10_000_000+1):
    s = str(i)
    while int(s)!=1 and int(s)!=89:
        s = str(sum([int(x)**2 for x in s]))
    if s=='89':
        n+=1
print(n)