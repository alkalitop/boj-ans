import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
A = list(map(int, input().split()))
b = list(map(int, input().split()))
B = deque()
m = int(input())
C = list(map(int, input().split()))

R = [0]*m

for i in range(n): not A[i] and B.append(b[i])
        
for i in range(m):
    B.appendleft(C[i])
    R[i] = B.pop()
    
print(*R)
