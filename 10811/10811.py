import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [i for i in range(1, n+1)]

for i in range(m):
    p, q = map(int, input().split())
    B = list(reversed(A[p-1:q]))
    for j in range(q-p+1):
        A[p-1+j] = B[j]
    
print(*A)
    
    
