from bisect import *

n = int(input())

seq = list(map(int, input().split()))
lis_pre = [-10**9-1]
lis_idx = []

for i in range(n):
    p = seq[i]
    if lis_pre[-1] < p:
        lis_pre.append(p)
        lis_idx.append((p, len(lis_pre)-1))
    else:
        k = bisect_left(lis_pre, p)
        lis_pre[k] = p
        lis_idx.append((p, k))

t = len(lis_pre)-1
print(t)

lis = []

for i in range(len(lis_idx)-1, -1, -1):
    if t == lis_idx[i][1]:
        lis.append(lis_idx[i][0])
        t -= 1
        
print(*reversed(lis))
