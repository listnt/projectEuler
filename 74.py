import math

d={}
n = 0 
for i in range(1,1000001):
    if i in d:
        continue
    
    d[i]=1
    
    s = str(i)
    visited = [i]
    
    while True:
        k=0
        for c in str(visited[-1]):
            k += math.factorial(int(c))
        if k in visited:
            break
        d[k] =1
        visited.append(k)
    if len(visited) == 60:
        n+=1
        
print(n)