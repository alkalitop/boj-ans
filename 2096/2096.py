n = int(input())

dp = list(map(int, input().split()))
dp.append(dp[0])
dp.append(dp[1])
dp.append(dp[2])

for i in range(1, n):
    s = list(map(int, input().split()))
    s.append(s[0])
    s.append(s[1])
    s.append(s[2])

    s[0] += max(dp[0], dp[1])
    s[1] += max(dp[0], dp[1], dp[2])
    s[2] += max(dp[1], dp[2])
    s[3] += min(dp[3], dp[4])
    s[4] += min(dp[3], dp[4], dp[5])
    s[5] += min(dp[4], dp[5])

    dp = s

print(max(*dp[:3]), min(*dp[3:]))
