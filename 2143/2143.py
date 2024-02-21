from bisect import *

import sys
input = sys.stdin.readline

t = int(input())

n = int(input())
A = [*map(int,input().split())]
SA = sorted(A + [sum(A[i:j+1]) for i in range(n) for j in range(i+1, n)])

m = int(input())
B = [*map(int,input().split())]
SB = sorted(B + [sum(B[i:j+1]) for i in range(m) for j in range(i+1, m)])

c = 0

for i in range(len(SA)):
    c += bisect_right(SB, t-SA[i]) - bisect_left(SB, t-SA[i])

print(c)
