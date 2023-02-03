import sys
input = sys.stdin.readline

q, m = map(int, input().split())

s = '1'
dp = [0, 1]
for i in range(3001):
    tmp = dp[0] + dp[1]
    dp[0] = dp[1]+0
    dp[1] = tmp%m
    if i > 0 and dp[0] == 0 and dp[1] == 1: break
    s += str(dp[1])

p = len(s)

for i in range(q):
	idx = (int(input())%p)-1
	print(s[idx])
