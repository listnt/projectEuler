def isPandigital(n):
    s = str(n)
    d=[0]*10
    for c in s:
        if c=='0':
            return False
        d[int(c)]+=1
    for k in d[1:]:
        if k!=1:
            return False
    return True

maxPandigital=123456789
for i in range(1,1000000):
    num = 0
    for n in range(1,10):
        newN = i*n
        num =num * 10**len(str(newN)) + newN
        if n==1:
            continue
        isPan = isPandigital(num)
        if isPan and num > maxPandigital:
            maxPandigital = num
        if num > 1000000000:
            break
print(maxPandigital)