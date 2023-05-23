m = 10**9+7

dp = [0]*16

dp[0] = 1
dp[1] = 3

for i in range(2, 16):
    dp[i] = 4*dp[i-1] - dp[i-2]
    dp[i] %= m

n = int(input())  

print(0 if n % 2 else dp[n>>1])
      
      
