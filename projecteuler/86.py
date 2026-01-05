import math

M=100
Ms=[1975]
for M in range(100,10000):
    n=0
    for i in range(2,2*M+1):
        shortest = math.isqrt(i*i + M*M)
        if shortest*shortest == i*i + M*M:
            low = max(1, i-M+1)
            high = min(M-1, i//2)
            partitions = max(0,high-low+1)
            
            n+=partitions
            
    for i in range(1,M):
        shortest = math.isqrt(M*M + (M+i)*(M+i))
        if shortest*shortest == M*M + (M+i)*(M+i):
            n+=1
    
    shortest = math.isqrt(5*M)
    if shortest*shortest == 5*M:
        n+=1
    
    n = n + Ms[-1]
    Ms.append(n)
    if n > 1000000:
        print(M)
        break