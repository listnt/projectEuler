def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
numsC = 1
primeC = 0

side = 3
while side <= 100000:
    p = (side-2)*4+4
    numsC += 4
    
    n1 =  (side-2)*(side-2)+p//2
    n2 =  (side-2)*(side-2)+p//4
    n3 =  (side-2)*(side-2)+3 * p//4
    if isPrime(n1):
        primeC += 1
    if isPrime(n2):
        primeC += 1
    if isPrime(n3):
        primeC += 1
    side += 2
    
    if numsC > 0:
        if primeC/numsC < 0.1:
            print(side)
            break