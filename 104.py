import math

prev2last9digits = 1
prevlast9digits = 1
last9digits = 0

prev2first9digits = 1
prevfirst9digits = 1
first9digits = 0

mod = int(10**9)

def isPandigital(n):
    s=sorted(list(str(n)))
    return ''.join(s) == '123456789'

i=2
while not isPandigital(int(first9digits)) or not isPandigital(int(last9digits)):
    i+=1
    
    x= i*math.log10((1+math.sqrt(5))/2)-math.log10(math.sqrt(5))
    f = x - math.floor(x)
    
    first9digits = int(10**(f+8))
    
    last9digits = (prev2last9digits + prevlast9digits) % mod
    prev2last9digits = prevlast9digits
    prevlast9digits = last9digits
print(i)