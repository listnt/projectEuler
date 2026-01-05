import math

triplets = []
for i in range(2,5000):
    for j in range(1,i):
        if math.gcd(i,j)==1 and ((i%2==1 and j%2==0) or (i%2==0 and j%2==1)):
            triplet = (i*i-j*j,2*i*j,i*i+j*j)
            if sum(triplet) > 1_500_000:
                break
            
            triplets.append(triplet)

d = {}
for triplet in triplets:
    i = 1
    s = sum(triplet)
    while s <= 1_500_000:
        if s not in d:
            d[s]=0
        d[s]+=1
        i+=1
        s=i*sum(triplet)

total=0
for n in d.keys():
    if d[n]==1:
        total+=1
print(total)