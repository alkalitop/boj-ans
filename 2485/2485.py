from math import gcd

n = int(input())

start = int(input())

pre = 0
cur = start

dist = []

for i in range(n-1):
    pre = cur
    cur = int(input())

    dist.append(cur - pre)

g = gcd(*dist)

print(sum(dist) // g - len(dist))
