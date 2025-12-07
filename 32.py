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

s="123456789"
s=list(s)
i=1

products = {}
while nextPermutation(s):
    i+=1
    multiplicand = 0
    multiplier = 1
    product = 1
    for i in range(1,8):
        multiplicand = s[:i]
        for j in range(i+1,9):
            multiplier=s[i:j]
            product = int(''.join(multiplicand)) * int(''.join(multiplier))
            expected = int(''.join(s[j:]))
            if product == expected:
                products[product] = 1

sun = 0
for k in products.keys():
    sun+=k
print(k)