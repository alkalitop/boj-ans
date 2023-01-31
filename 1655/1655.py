from heapq import *
import sys

input = sys.stdin.readline

maxhp = []
minhp = []

def maxhp_get(t):
    return maxhp[t][1]

for i in range(int(input())):
    k = int(input())
    if len(maxhp) == len(minhp):
        heappush(maxhp, (-k, k))
    else:
        heappush(minhp, k)
    if i > 0 and maxhp_get(0) > minhp[0]:
        p = maxhp_get(0)
        q = minhp[0]
        heappop(maxhp)
        heappop(minhp)
        heappush(maxhp, (-q, q))
        heappush(minhp, p)
    print(maxhp_get(0))
     
    
