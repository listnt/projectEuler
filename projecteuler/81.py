A = []
for line in open('0081_matrix.txt'):
    A.append([int(x) for x in line.split(',')])

for i in range(80):
    for j in range(80):
        if i == 0 and j == 0:
            continue
        if i == 0:
            A[i][j] += A[i][j-1]
        elif j==0:
            A[i][j] += A[i-1][j]
        else:
            A[i][j] += min(A[i-1][j], A[i][j-1])
print(A[79][79])