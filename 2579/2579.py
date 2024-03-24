n = int(input())
s = [int(input()) for _ in range(n)]

dp = [0]*n

if n >= 2:
    dp[0] = s[0]
    dp[1] = s[0]+s[1]
    for i in range(2, n):
        dp[i] = s[i] + max(dp[i-2], s[i-1] + dp[i-3])
    print(dp[-1])
else:
    print(s[0])
