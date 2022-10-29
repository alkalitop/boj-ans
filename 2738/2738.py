import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [None]*n
B = [None]*n
C = [None]*n

for i in range(n):
    A[i] = list(map(int, input().split()))
for i in range(n):
    B[i] = list(map(int, input().split()))
    
for i in range(n):
    C[i] = [None]*m
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]

for a in C:
    print(' '.join(list(map(str, a))))
