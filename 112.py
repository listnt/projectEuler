def isIncreasing(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            return False
    return True

def isDecreasing(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i]<s[i+1]:
            return False
    return True

def isBouncy(n):
    return not(isIncreasing(n) or isDecreasing(n))

n=0
for i in range(1,10000000):
    if isBouncy(i):
        n+=1
    if n/i>=0.99:
        print(i)
        break