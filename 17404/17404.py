import sys, math
input = sys.stdin.readline

n = int(input())

pu = [list(map(int, input().split())) for _ in range(n)]
c = math.inf

for i in range(3):
    dp = [[math.inf]*3 for _ in range(n)]
    dp[0][i] = pu[0][i]
    
    for j in range(1, n):
        dp[j][0] = pu[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = pu[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = pu[j][2] + min(dp[j-1][0], dp[j-1][1])

    del dp[-1][i]
    c = min(c, min(*dp[-1]))

print(c)
