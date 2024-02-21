from bisect import *

n = int(input())

seq = [0]*n

for i in range(n):
    a, b = map(int, input().split())
    seq[i] = (b, a)

seq.sort()

for i in range(n):
    seq[i] = seq[i][1]

lis_pre = [0]
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
print(n-t)

lis = []

for i in range(len(lis_idx)-1, -1, -1):
    if t == lis_idx[i][1]:
        lis.append(lis_idx[i][0])
        t -= 1

for v in sorted([*(set(seq)-set(lis))]):
    print(v)
