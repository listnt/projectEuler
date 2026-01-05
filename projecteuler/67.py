import heapq
import sys

triangle=open("0067_triangle.txt").read()

triangle = triangle.split('\n')
triangle = [list(map(int, line.split(' '))) for line in triangle]
total = sum([len(row) for row in triangle])

for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        if j==0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j == len(triangle[i-1]):
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])
            
print(max(triangle[-1]))