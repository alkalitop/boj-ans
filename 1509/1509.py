s = input()
n = len(s)

dp = [2500 for _ in range(n+1)]
dp[-1] = 0
p = [[0]*n for _ in range(n)]

for i in range(n):
    if i < n-1:
        p[i][i+1] = int(s[i] == s[i+1])
    p[i][i] = 1

for k in range(n-2):
    for i in range(n-k-2):
        j = i+k+2
        p[i][j] = int(s[i] == s[j] and p[i+1][j-1])

for j in range(n):
    for i in range(j+1):
        if p[i][j]:
            dp[j] = min(dp[j], dp[i-1]+1)
        else:
            dp[j] = min(dp[j], dp[j-1]+1)

print(dp[n-1])
