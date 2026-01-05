import fractions

def seq2(n):
    return 1 if n==0 else 2

def eseq(n):
    return 2 if n==0 else 1 if n%3!=2 else(n+1)//3<<1

def approxe(n):
    frac = fractions.Fraction(1,eseq(n))
    for i in range(n-1,0,-1):
        frac = fractions.Fraction(1,eseq(i)+frac)
    return frac+eseq(0)
    
def approx2(n):
    frac = fractions.Fraction(1,seq2(n))
    for i in range(n-1,0,-1):
        frac = fractions.Fraction(1,seq2(i)+frac)
    print(frac+seq2(0))
    
for i in range(100):
    frac = approxe(i)
    print(i+1, sum([int(x) for x in str(frac.numerator)]))