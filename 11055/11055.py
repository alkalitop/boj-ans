n = int(input())
seq = [*map(int, input().split())]
dp = [0]*n

for i in range(n):
    dp[i] = seq[i]
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+seq[i])
            
print(max(dp))
    
