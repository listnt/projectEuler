def colatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
    
maxLen = 0
for i in range(13,1000000):
    len=1
    term = colatz(i)
    while term != 1:
        term = colatz(term)
        len += 1
    if len > maxLen:
        maxLen = len
        print(i,maxLen)