def nextPermutation(s):

    n = len(s)

    # Find the rightmost character which is
    # smaller than its next character
    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    # If no such character found, all permutations done
    if i < 0:
        return False

    # Find the ceiling of s[i]
    j = n - 1
    while j > i and s[j] <= s[i]:
        j -= 1

    # Swap the found characters
    s[i], s[j] = s[j], s[i]

    # Sort (reverse) the substring after index i
    s[i + 1:] = reversed(s[i + 1:])

    return True

s="0123456789"
s=list(s)
i=1
while nextPermutation(s):
    # print("".join(s))
    i+=1
    if i==1000000:
        print("".join(s))
        break