import sys
input = sys.stdin.readline

n = int(input())
A = [0]*n

for i in range(n):
    A[i] = int(input())
    
i = n-1
cnt = 0
while i > 0:
    if A[i-1] >= A[i]:
        cnt += A[i-1]-A[i]+1
        A[i-1] = A[i]-1
    i -= 1
        
print(cnt)
