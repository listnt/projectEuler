import numpy as np

def stationary_distribution(P):
    eigvals, eigvecs = np.linalg.eig(P.T)
    idx = np.argmin(np.abs(eigvals - 1))
    pi = np.real(eigvecs[:, idx])
    pi = pi / pi.sum()
    return pi

import collections

dice = [d1+d2 for d1 in range(1,7) for d2 in range(1,7)]
counts = collections.Counter(dice)
print(counts)

cc = [2,17,33]
ch = [7,22,36]


def comunityChest(idx):
    pp = [0]*40
    pp[0]=1/16
    pp[10]=1/16
    pp[idx]=14/16
    return pp

def chance(idx):
    pp = [0]*40
    pp[0]=1/16
    pp[10]=1/16
    pp[11]=1/16
    pp[24]=1/16
    pp[39]=1/16
    pp[5]=1/16
    nextR = 5
    if idx<5:
        nextR = 5
    elif idx<15:
        nextR = 15
    elif idx<25:
        nextR = 25
    elif idx<35:
        nextR = 35
    else:
        nextR = 5
    pp[nextR]+=2/16
    
    nextU = 12
    if idx<12:
        nextU = 12
    elif idx<28:
        nextU = 28
    else:
        nextU = 12
    pp[nextU]+=1/16
    
    if idx==36:
        pp[0]+=1/16*1/16
        pp[10]+=1/16*1/16
        pp[33]+=1/16*14/16
    else:
        pp[idx-3]+=1/16
        
    pp[idx]+=6/16
    
    return pp


n=36


markov = []
prob = [0]*40

for i in range(40):
    for path in counts.keys():
        tile = (path+i)%40
        prob[tile]+=(counts[path]*6)/(6*n+1)
        if tile in cc or tile in ch:
            newProb = comunityChest(tile) if tile in cc else chance(tile)
            for j in range(40):
                prob[j] += prob[tile]*newProb[j]
        elif tile==30:
            prob[10]+=prob[tile]
            prob[tile]=0
    prob[10]+=1/217
    markov.append(prob)
    prob = [0]*40

dist = stationary_distribution(np.array(markov))
d = [(i,dist[i]) for i in range(40)]
d.sort(key=lambda x:x[1],reverse=True)

for j,d in d:
    print(f"{j}:{d}",end=" ")
print()