import math
def isTriangle(t):
    k = math.isqrt(1+8*t)
    n = (k - 1)//4
    if n*(n-1)//2 == t:
        return True
    return False

def isSquare(s):
    k = math.isqrt(s)
    if k*k == s:
        return True
    return False

def isPentagonal(p):
    k = math.isqrt(1+24*p)
    n = (1 + k)//6
    if n*(3*n-1)//2 == p:
        return True
    return False

def isHexagonal(h):
    k = math.isqrt(1+8*h)
    n = (1 + k)//4
    if n*(2*n-1) == h:
        return True
    return False

def isHeptagonal(h):
    k = math.isqrt(9+40*h)
    n = (3 + k)//10
    if n*(5*n-3)//2 == h:
        return True
    return False

def isOptogonal(o):
    k = math.isqrt(4+12*o)
    n = (2 + k)//6
    if n*(3*n-2) == o:
        return True
    return False

d={}

for i in range(1,1000):
    t = i*(i+1)//2
    if 1000<=t<=9999:
        s = str(t)
        s = list(s)
        s[2]="*"
        s[3]="*"
        if ''.join(s) not in  d:
            d[''.join(s)] = []
        d[''.join(s)].append((t,"t",i))
    
    t = i*i
    if 1000<=t<=9999:
        s = str(t)
        s = list(s)
        s[2]="*"
        s[3]="*"
        if ''.join(s) not in  d:
            d[''.join(s)] = []
        d[''.join(s)].append((t,"s",i))

    
    t = i*(3*i-1)//2
    if 1000<=t<=9999:
        s = str(t)
        s = list(s)
        s[2]="*"
        s[3]="*"
        if ''.join(s) not in  d:
            d[''.join(s)] = []
        d[''.join(s)].append((t,"p",i))

    
    t = i*(2*i-1)
    if 1000<=t<=9999:
        s = str(t)
        s = list(s)
        s[2]="*"
        s[3]="*"
        if ''.join(s) not in  d:
            d[''.join(s)] = []
        d[''.join(s)].append((t,"hex",i))

    
    t = i*(5*i-3)//2
    if 1000<=t<=9999:
        s = str(t)
        s = list(s)
        s[2]="*"
        s[3]="*"
        if ''.join(s) not in  d:
            d[''.join(s)] = []
        d[''.join(s)].append((t,"hep",i))

    
    t = i*(3*i-2)
    if 1000<=t<=9999:
        s = str(t)
        s = list(s)
        s[2]="*"
        s[3]="*"
        if ''.join(s) not in  d:
            d[''.join(s)] = []
        d[''.join(s)].append((t,"o",i))

for k in sorted(d.keys()):
    print(k,d[k])

def fun(i,indexes,visited,ans):
    if len(visited)==6:
        last = str(ans[-1])
        first = str(ans[0])
        if last[2]!=first[0] or last[3]!=first[1]:
            return
        print(ans,visited,indexes,sum(ans))
        return
    s = str(i)
    s=list(s)
    if f"{s[2]}{s[3]}**"not in d:
        return
    for j in d[f"{s[2]}{s[3]}**"]:
        if j[1] in visited:
            continue
        fun(j[0],indexes + [j[2]],visited+[j[1]],ans+[j[0]])

for i in range(1,1000):
    t = i*(i+1)//2
    if 1000<=t<=9999:
        visited = ["t"]
        ans = [t]
        indexes=[i]
        fun(t,indexes,visited,ans)