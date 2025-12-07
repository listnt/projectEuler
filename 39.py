maxSols = 0 
maxP = 0
for p in range(3,1001):
    sols = 0
    for a in range(1,p-1):
        for b in range(1,p-a):
            c = p-a-b
            if a*a + b*b == c*c :
                sols += 1
                # print(p,a,b,c)
    if sols > maxSols:
        maxSols=sols
        maxP = p
print(maxP)