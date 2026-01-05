def divisors(n):
    divs = [1]
    root = int(n**0.5)
    for i in range(2, root + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)
    if root * root == n:
        divs = divs[:-1]  # perfect square fix
    return divs

abundants={}
for i in range(30000):
    divs = divisors(i)
    if sum(divs)> i:
        abundants[i]=1

sun = 0
for i in range(30000):
    flag = False
    for j in range(0,i):
        if j in abundants and (i-j) in abundants:
            flag=True
    if not flag:
        sun+=i
print(sun)