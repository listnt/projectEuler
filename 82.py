import numpy as np

f = open("0082_matrix.txt")

M = []
for line in f:
    M.append([int(x) for x in line.split(",")])

M = np.array(M)

for col in range(1,80):
    coll = M[:,col]
    for i in range(0,80):
        end = 79-i
        start = i
        for j in range(start+1,end):
            if j == 79:
                coll[j]=min(coll[j-1]+coll[j],coll[j]+M[j][col-1])
            else:
                coll[j]=min(coll[j-1]+coll[j],coll[j]+M[j][col-1])
        for j in range(end-1,start,-1):
            if j == 0:
                coll[j]=min(coll[j]+coll[j+1],coll[j]+M[j][col-1])
            else:
                coll[j]=min(coll[j]+coll[j+1],coll[j]+M[j][col-1])
    M[:,col]=coll
mins=int(10**9)
for i in range(80):
    mins=min(M[i][79],mins)
print(mins)