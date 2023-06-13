n = int(input())

A = list(map(int, input().split()))
dp1 = [0]*n
dp2 = [0]*n

for i in range(n):
    dp1[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

for i in range(n-1, -1, -1):
    dp2[i] = 1
    for j in range(n-1, i, -1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
            
c = 0
for i in range(n):
    c = max(c, dp1[i]+dp2[i]-1)
    
print(c)


