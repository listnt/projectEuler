def isPalindrome(n):
    return str(n) == str(n)[::-1]
def reverse(n):
    return int(str(n)[::-1])


lychrelCount = 0
for i in range(10000):
    n=i
    isLychrel = True
    for j in range(50):
        n = n+reverse(n)
        if isPalindrome(n):
            isLychrel = False
            break
    if isLychrel:
        lychrelCount+=1
print(lychrelCount)