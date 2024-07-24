from bisect import *
import sys

input = sys.stdin.readline

n = int(input())

A = [0]*n
B = [0]*n
C = [0]*n
D = [0]*n

for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, input().split())

P = [0]*(n**2)
Q = [0]*(n**2)

k = 0
for i in range(n):
    for j in range(n):
        P[k] = A[i] + B[j]
        Q[k] = C[i] + D[j]
        k += 1

P.sort()
Q.sort()

ans = 0

for v in P:
    ans += bisect_right(Q, -v) - bisect_left(Q, -v)

print(ans)
