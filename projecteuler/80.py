from decimal import Decimal, localcontext, getcontext
NumberType = int | float | Decimal

def sqrt_Heron(
    s: NumberType,
    precision: int | None = None,
    guess: NumberType | None = None
) -> Decimal:
    if s == 0:
        return Decimal(0)
    s = Decimal(s)

    if s < 0:
        raise ValueError("sqrt(s) is not defined for negative numbers.")

    if precision is None:
        precision = getcontext().prec  # use current global context if not specified

    # Silently enforce minimum precision
    if precision == 1:
        precision = 2

    guess = Decimal(s / 2 if guess is None else guess)
    guard = 25  # temporary extra digits for internal stability
    max_iter = 10_000

    # Local context: isolate precision changes
    with localcontext() as ctx:
        ctx.prec = precision + guard
        guess = (guess + s / guess) / 2
        for _ in range(max_iter):
            next_guess = (guess + s / guess) / 2

            # Stop when improvement is small enough
            if guess - next_guess < Decimal(f"1e-{precision}"):
                break
            guess = next_guess
        else:
            raise ArithmeticError(f"Heron method did not converge within {max_iter} iterations")

        # Round to target precision (getting rid of guard)
        ctx.prec = precision
        return +next_guess
import math
n = 0
for i in range(2,100):
    guess = math.isqrt(i)
    if guess*guess == i:
        continue
    
    digits = sqrt_Heron(i,300)
    counted = 0
    for d in str(digits):
        if d == '.':
            continue
        counted += 1
        if counted > 100:
            break
        n+=int(d)
print(n)