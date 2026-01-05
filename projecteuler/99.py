import math
f = open("0099_base_exp.txt")
nums = []
for i,line in enumerate(f):
    a,b = map(int, line.split(","))
    nums.append((a,b,i+1))
nums.sort(key=lambda x: x[1]*math.log(x[0]))
print(nums[-1])