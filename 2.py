arr=[]
arr.append(1)
arr.append(1)
while arr[-1] <= 4000000:
    arr.append(arr[-1]+arr[-2])
print(arr)
sum =0
for v in arr:
    if v%2==0:
        sum+=v
print(sum)