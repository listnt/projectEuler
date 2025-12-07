def isPalindrome10(n):
    return str(n) == str(n)[::-1]

def isPalindromeinBinary(n):
    return bin(n)[2:] == bin(n)[2:][::-1]

sun = 0
for i in range(1,1000000):
    if isPalindrome10(i) and isPalindromeinBinary(i):
        sun+=i
print(sun)