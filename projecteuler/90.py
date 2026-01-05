import itertools

arr=[0,1,2,3,4,5,6,7,8,9]
squares = [[0,1],[0,4],[0,9],[1,6],[2,5],[3,6],[4,9],[6,4],[8,1]]


n=0
for comb1 in itertools.combinations(arr,6):
    for comb2 in itertools.combinations(arr,6):
        ss = 0
        for s in squares:
            if (s[0] in comb1 and s[1] in comb2) or (s[0] in comb2 and s[1] in comb1):
                ss+=1
            elif (s[0]==6 and 9 in comb1 and s[1] in comb2) or (s[0]==6 and 9 in comb2 and s[1] in comb1):
                ss+=1
            elif (s[0]==9 and 6 in comb1 and s[1] in comb2) or (s[0]==9 and 6 in comb2 and s[1] in comb1):
                ss+=1
            elif (s[1]==6 and 9 in comb1 and s[0] in comb2) or (s[1]==6 and 9 in comb2 and s[0] in comb1):
                ss+=1
            elif (s[1]==9 and 6 in comb1 and s[0] in comb2) or (s[1]==9 and 6 in comb2 and s[0] in comb1):
                ss+=1
        if ss != len(squares):
            continue
        n+=1
print(n//2)