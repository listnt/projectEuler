import math

coins=[1,2,5,10,20,50,100,200]
def count_ways(target, coins):
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]


print(count_ways(1,coins))
print(count_ways(2,coins))
print(count_ways(3,coins))
print(count_ways(4,coins))
print(count_ways(5,coins))

print(count_ways(200,coins))