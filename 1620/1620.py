import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = {}
B = [0]*n

for i in range(n):
    q = input()
    A[q] = i
    B[i] = q
	
for j in range(m):
    q = input()
    if q in A:
        print(A[q]+1)
    else:
        print(B[int(q)-1].rstrip())
