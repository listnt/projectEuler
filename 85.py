closest = 0
closesi = 0
closestj = 0
for i in range(1,1000):
    for j in range(1,1000):
        nums = i*(i+1)*j*(j+1)/4
        if abs(2_000_000-nums) < abs(2_000_000-closest):
            closest, closesi, closestj = nums, i, j
print(closesi*closestj,closest)