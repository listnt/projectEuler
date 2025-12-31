n=0
f = open("0102_triangles.txt")
for line in f:
    coords = list(map(int, line.strip().split(",")))
    A,B,C = [[coords[0],coords[1]],[coords[2],coords[3]],[coords[4],coords[5]]]
    denom = (B[1]-C[1])*(A[0]-C[0])+(C[0]-B[0])*(A[1]-C[1])
    lambda1 = ((B[1]-C[1])*(-C[0])+(C[0]-B[0])*(-C[1]))/denom
    lambda2 = ((C[1]-A[1])*(-C[0])+(A[0]-C[0])*(-C[1]))/denom
    lambda3 = 1-lambda1-lambda2
    
    if lambda1>=0 and lambda1<=1 and lambda2>=0 and lambda2<=1 and lambda3>=0 and lambda3<=1:
        n+=1
print(n)