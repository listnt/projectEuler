def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nextPermutation(s):
    n = len(s)
    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i < 0:
        return False
    j = n - 1
    while j > i and s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = reversed(s[i + 1:])
    return True

s="0123456789" 
s=list(s)


total = 0
while nextPermutation(s):
    if int(''.join(s[1:4])) % 2 == 0 and int(''.join(s[2:5])) % 3 == 0 and int(''.join(s[3:6])) % 5 == 0 and int(''.join(s[4:7])) % 7 == 0 and int(''.join(s[5:8])) % 11 == 0 and int(''.join(s[6:9])) % 13 == 0 and int(''.join(s[7:10])) % 17 == 0:
        total += int(''.join(s))
print(total)