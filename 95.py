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
longestChain=0
longestA = []
for i in range(2,1000001):
    divs = divisors(i)
    visited = [i]
    while True:
        if len(divs)==0:
            visited=[]
            break
        if sum(divs)>1000000:
            visited=[]
            break
        if sum(divs) in visited:
            if sum(divs)!=visited[0]:
                visited=[]
            break
        visited.append(sum(divs))
        divs = divisors(sum(divs))
        
    if len(visited) > longestChain:
        print(i,list(sorted(visited)))
        longestChain = len(visited)
        longestA = visited
print(longestChain,longestA)