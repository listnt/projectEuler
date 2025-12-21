sun = 0
for i in range(100):
    for j in range(100):
        digitsSum = sum([int(c) for c in str(i**j)])
        if digitsSum > sun:
            sun = digitsSum
print(sun)