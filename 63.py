n=0
for i in range(1,10):
    for j in range(1,100):
        if len(str(i**j))==j:
            n+=1
print(n)