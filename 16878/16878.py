import sys
input = sys.stdin.readline

dp = [0]*(10**7+1)
dp[0] = 1
dp[1] = 1
dp[4] = 2

m = 1000000007

for i in range(5, 10**7+1):
    p = (i+1)*(dp[i-1]%m)%m
    q = (i-2)*(dp[i-2]%m)%m
    r = (i-5)*(dp[i-3]%m)%m
    s = (i-3)*(dp[i-4]%m)%m
    dp[i] = (((p-q)%m)-((r-s)%m))%m
    
for i in range(int(input())):
    print(dp[int(input())])
