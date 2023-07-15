import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    
    dp = [list(map(int, input().split())), list(map(int, input().split())), [0]*n]

    for i in range(1, n):
        dp[0][i] += max(dp[1][i-1], dp[2][i-1])
        dp[1][i] += max(dp[0][i-1], dp[2][i-1])
        dp[2][i] += max(dp[0][i-1], dp[1][i-1], dp[2][i-1])

    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))
