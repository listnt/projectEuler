f = open("0098_words.txt").read()

words = [word.strip('"') for word in  f.split(",")]

d = {}

for word in words:
    anagram = ''.join(tuple(sorted(word)))
    if anagram not in d:
        d[anagram]=[]
    d[anagram].append(word)
keys = list(d.keys())
for a in keys:
    if len(d[a])==1:
        del d[a]
        

import itertools
import numpy
import math

ds =[0,1,2,3,4,5,6,7,8,9]

for a in d.keys():
    for comb in itertools.combinations(d[a],2):
        un = numpy.unique(list(a))
        w1=comb[0]
        w2=comb[1]
        for perm in itertools.permutations(ds,len(un)):
            sub = {}
            for i in range(len(un)):
                sub[un[i]]=perm[i]
            num1 = ""
            num2 = ""
            for c in w1:
                num1+=str(sub[c])
            if num1[0]=='0':
                continue
            for c in w2:
                num2+=str(sub[c])
            if num2[0]=='0':
                continue
            num1 = int(num1)
            num2 = int(num2)
            
            sq1 = math.isqrt(num1)
            if sq1*sq1 != num1:
                continue
            
            sq2 = math.isqrt(num2)
            if sq2*sq2 != num2:
                continue
            print(w1,w2,num1,num2)