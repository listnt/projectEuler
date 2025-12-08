pentag = []
pentags = {}
for i in range(1,10000):
    pent = i*(3*i-1)//2
    pentag.append(pent)
    pentags[pent]=1
    

for i in range(len(pentag)):
    p1 = pentag[i]
    for j in range(i+1, len(pentag)):
        p2 = pentag[j]
        if p1 + p2 in pentags and p2-p1 in pentags:
            print(p1,p2) 