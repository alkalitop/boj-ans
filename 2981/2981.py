import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
S = []

prev = 0
for i in range(n):
    if i == 0:
        prev = int(input())
        continue
    else:
        cur = int(input())
        S.append(int(abs(cur-prev)))
        prev = cur

g = gcd(*S)
k = 2

M = set()
while k**2<=g:
    if g % k == 0:
        M.add(k)
        M.add(g//k)
    k += 1 
    
M.add(g)
print(*sorted(list(M)))
