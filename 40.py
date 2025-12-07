s=""
for i in range(1,500000):
    s+=str(i)
res = 1
for i in range(0,7):
    res *= int(s[10**i-1])
print(res)