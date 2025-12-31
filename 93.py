def add(n,m):
    return n+m

def sub(n,m):
    return n-m

def mul(n,m):
    return n*m

def div(n,m):
    return n/m

operations = [add,sub,mul,div]

import numpy
from itertools import product
import fractions


maxChain = 0
maxA=()
dict = {}
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                un = numpy.unique([a,b,c,d])
                if len(un) != 4:
                    continue
                for ops in product(operations,repeat=3):
                    af = fractions.Fraction(a,1)
                    bf = fractions.Fraction(b,1)
                    cf = fractions.Fraction(c,1)
                    df = fractions.Fraction(d,1)
                    try:
                        idx = tuple(sorted([a,b,c,d]))
                        
                        res = ops[2](ops[1](ops[0](af,bf),cf),df)
                        if res.denominator == 1:
                            if idx not in dict:
                                dict[idx] = {}
                            dict[idx][res.numerator]=1
                        res = ops[2](ops[0](a,b),ops[1](c,d))
                        if res.denominator == 1:
                            if idx not in dict:
                                dict[idx] = {}
                            dict[idx][res.numerator]=1
                    except:
                        continue
for idx in dict.keys():
    arr = dict[idx]
    aaaa = list(sorted(dict[idx].keys()))
    for i in range(1,1000):
        if i in arr:
            if i>=maxChain:
                maxChain = i
                maxA = idx
        else:
            break

print(''.join([str(x) for x in maxA]))