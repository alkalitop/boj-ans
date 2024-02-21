import sys
input = sys.stdin.readline

n = int(input())
s = [*map(int, input().split())]

dp = [[0]*n for _ in range(n)]

for i in range(n):
    if i < n-1:
        dp[i][i+1] = int(s[i] == s[i+1])
    dp[i][i] = 1

for k in range(n-2):
    for i in range(n-k-2):
        j = i+k+2
        dp[i][j] = int(s[i] == s[j] and dp[i+1][j-1])

m = int(input())
for i in range(m):
    p, q = map(int, input().split())
    print(dp[p-1][q-1])
