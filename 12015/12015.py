from bisect import *

n = int(input())

seq = list(map(int, input().split()))
lis = [0]

for i in range(n):
    p = seq[i]
    if lis[-1] < p:
        lis.append(p)
    else:
        lis[bisect_left(lis, p)] = p

print(len(lis)-1)
