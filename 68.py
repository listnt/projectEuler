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

maxN = 0
s = [1,2,3,4,5,6,7,8,9,10]
while nextPermutation(s):
    g0 = s[0]+s[1]+s[7]
    g1 = s[1]+s[2]+s[8]
    g2 = s[2]+s[3]+s[9]
    g3 = s[3]+s[4]+s[5]
    g4 = s[4]+s[0]+s[6]
    if g0 != g1 or g1 != g2 or g2 != g3 or g3 != g4 or g4 != g0:
        continue
    groups = [(s[0],s[1],s[7]),(s[1],s[2],s[8]),(s[2],s[3],s[9]),(s[3],s[4],s[5]),(s[4],s[0],s[6])]
    minIdx = 0
    for i,g in enumerate(groups):
        if g[2]<groups[minIdx][2]:
            minIdx = i
    N = ""
    for i in range(len(groups)):
        idx = minIdx - i
        N += (''.join([ str(x) for x in groups[idx][::-1]]))
    N = int(N)
    if N>maxN and len(str(N))==16:
        print(N)
        maxN = N