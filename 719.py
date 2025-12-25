def has_valid_split(s, target):
    n = len(s)

    def backtrack(index, current_sum):
        # Prune if sum already too large
        if current_sum > target:
            return False

        # If consumed all digits, check sum
        if index == n:
            return current_sum == target

        value = 0
        for i in range(index, n):
            value = value * 10 + int(s[i])
            if backtrack(i + 1, current_sum + value):
                return True

        return False

    return backtrack(0, 0)

import math
n=0
for i in range(2,int(math.sqrt((10**12))+1)):
    s = i**2
    if s>int((10**12)):
        break
    
    if has_valid_split(str(s), i):
        n += s
print(n)