
cubes = {}
for i in range(10000):
    cub = sorted(list(str(i*i*i)))
    if ''.join(cub) not in cubes:
        cubes[''.join(cub)] = [0]
    cubes[''.join(cub)][0]+=1
    cubes[''.join(cub)].append(i)

for cub in cubes.keys():
    if cubes[cub][0] == 5:
        print(cubes[cub])