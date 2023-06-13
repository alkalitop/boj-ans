import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*n

for i in range(n):
    dp[i] = list(map(int, input().split()))
    
for i in range(n-1, 0, -1):
    for j in range(i):
        dp[i-1][j] += max(dp[i][j], dp[i][j+1])
        
print(dp[0][0])
