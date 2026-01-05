import fractions


mem = [0]*1000
def continuedFraction(levels = 50):
    if levels == 1:
        return fractions.Fraction(1,2)
    if mem[levels]!=0:
        return mem[levels]
    mem[levels] = 1/( 2 + continuedFraction(levels-1))
    return mem[levels]

c = 0
for i in range(1,1000):
    frac =1 + continuedFraction(i)
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        c+=1
print(c)