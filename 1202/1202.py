from heapq import *

n, k = map(int, input().split())

gem = [0]*n
bag = [0]*k

c = 0

for i in range(n):
    m, v = map(int, input().split())
    gem[i] = (m, v)

for i in range(k):
    bag[i] = int(input())

gem.sort()
bag.sort()

q = []

for i in range(k):
    while gem and bag[i] >= gem[0][0]:
        heappush(q, -gem[0][1])
        heappop(gem)
    if q:
        c += -heappop(q)

print(c)
