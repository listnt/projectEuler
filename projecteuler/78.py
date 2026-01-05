from sympy.functions.combinatorial.numbers import partition

n=1
while True:
    parts = partition(n)
    if parts%1000000==0:
        print(n)
        break
    n+=1