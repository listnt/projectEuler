from fractions import Fraction
from collections.abc import Generator

def farey_sequence(n: int, descending: bool = False) -> Generator[Fraction]:
    a, b, c, d = 0, 1, 1, n
    if descending:
        a, c = 1, n - 1
    yield Fraction(a, b)
    while 0 <= c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        yield Fraction(a, b)

a,b = 1,3
c,d = 1,2

num = 0
for frac in farey_sequence(12000):
    if frac > Fraction(a,b) and frac < Fraction(c,d):
        num+=1
print(num)