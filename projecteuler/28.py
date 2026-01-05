side = 3
res = 1
p = 1
while side <= 1001:
    p = (side-2)*4+4
    res += side*side
    res += (side-2)*(side-2)+p//2
    res += (side-2)*(side-2)+p//4
    res += (side-2)*(side-2)+3 * p//4
    
    side += 2
    print(res)
print(res)