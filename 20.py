import math

s = math.factorial(100)
sum=0
for c in str(s):
    sum += int(c)
print(sum)