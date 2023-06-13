n = int(input())

A = list(map(int, input().split()))
dp = [0]*n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j]+1)
                
print(max(dp))
