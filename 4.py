def isPalindrome(n):
    return str(n) == str(n)[::-1]

maxPal=0    
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
        if isPalindrome(i*j):
            if i*j>maxPal:
                maxPal=i*j
print(maxPal)