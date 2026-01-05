import numpy as np
import random

import collections

D = 4
dice = [d1+d2 for d1 in range(1,D+1) for d2 in range(1,D+1)]
counts = collections.Counter(dice)
print(counts)

cc = [2,17,33]
ch = [7,22,36]


chanceC = [i for i in range(16)]
commC = [i for i in range(16)]

def comunityChest(idx):
    global commC
    
    card = commC[0]
    
    commC = commC[1:] + [commC[0]]
    
    if card==0:
        return 0
    elif card==1:
        return 10
    else:
        return idx

def chance(idx):
    global chanceC
    
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
    
    nextU = 12
    if idx<12:
        nextU = 12
    elif idx<28:
        nextU = 28
    else:
        nextU = 12
    
    card = chanceC[0]
    
    chanceC = chanceC[1:] + [chanceC[0]]
    
    if card==0:
        return 0
    elif card==1:
        return 10
    elif card==2:
        return 11
    elif card==3:
        return 24
    elif card==4:
        return 39
    elif card==5:
        return 5
    elif card==6:
        return nextR
    elif card==7:
        return nextR
    elif card==8:
        return nextU
    elif card==9:
        if idx==36:
            return comunityChest(idx)
        else:
            return idx-3
    else:
        return idx


n=36


markov = []
prob = [0]*40

doubles = 0

i=0

for _ in range(1000000):
    d1 = random.randint(1,D)
    d2 = random.randint(1,D)
    if d1==d2:
        doubles+=1
    else:
        doubles=0
    path = d1+d2
    i=(path+i)%40
    if doubles==3:
        i=10
        doubles=0
    if i in cc or i in ch:
        i = comunityChest(i) if i in cc else chance(i)
    elif i==30:
        i=10
    prob[i]+=1
    
def normalize(prob):
    s = sum(prob)
    return [x/s for x in prob]

prob = normalize(prob)

prob = [(i,p) for i,p in enumerate(prob)]
prob.sort(key=lambda x:x[1],reverse=True)

for j,p in prob:
    print(f"{j}:{p}",end=" ")
print()