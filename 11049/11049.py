import sys
input = sys.stdin.readline

n = int(input())

mx = [[*map(int, input().split())] for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for m in range(n-1):
    for i in range(n-m-1):
        j = i+m+1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], mx[i][0]*mx[k][1]*mx[j][1] + dp[i][k] + dp[k+1][j])

print(dp[0][-1])
