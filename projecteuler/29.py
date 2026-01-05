d={}
for a in range(2,101):
    for b in range(2,101):
        d[a**b]=1
print(len(d))