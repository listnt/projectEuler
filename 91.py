def isRightTriangle(P,Q,R):
    PQ = (P[0]-Q[0])*(P[0]-Q[0])+(P[1]-Q[1])*(P[1]-Q[1])
    QR = (Q[0]-R[0])*(Q[0]-R[0])+(Q[1]-R[1])*(Q[1]-R[1])
    RP = (R[0]-P[0])*(R[0]-P[0])+(R[1]-P[1])*(R[1]-P[1])
    sides = [PQ,QR,RP]
    sides.sort()
    if sides[0]+sides[1]==sides[2]:
        return True
    return False
    

total=0
for n in range(0,51):
    for m in range(0,51):
        for i in range(0,51):
            for j in range(0,51):
                P = (n,m)
                Q = (i,j)
                if P==(0,0) or Q==(0,0) or P==Q:
                    continue
                if isRightTriangle((0,0),P,Q):
                    total+=1
print(total//2)