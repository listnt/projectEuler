facts = [0]*10
facts[1]=1
facts[0]=1
def factorial(n):
    if n == 1:
        return 1
    if facts[n] != 0:
        return facts[n]
    res = n * factorial(n-1)
    facts[n]=res
    return res

for i in range(1,10):
    factorial(i)

sun = 0
for n in range(3,1000000): # it is correct cause 9! around 360k, so after 1 million there is no such number, proofing it i won't do
    s = str(n)
    res = 0 
    for c in s:
        res += facts[int(c)]
    if res == n:
        print(n)
        
        sun+=n
print(sun)