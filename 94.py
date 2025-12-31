import math

total=0
for i in range(2,10000):
    for j in range(1,i):
        if math.gcd(i,j)==1 and ((i%2==1 and j%2==0) or (i%2==0 and j%2==1)):
            triplet = (i*i-j*j,2*i*j,i*i+j*j)
            p = 2*triplet[2]+2*triplet[0]
            if p >= 1_000_000_000:
                break
            if triplet[0]*2==triplet[2]:
                continue
            k=1_000_000_000/(triplet[2]*2+triplet[0]*2)
            
print(total)
