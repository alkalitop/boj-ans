def eratosthenes(M):
    ret = [1]*(M+1)
    ret[0], ret[1] = (0, 0)
    p = 2
    while p in range(int(M**0.5)+1):
        if ret[p]:
            ret[p] = 1
            i = 2
            while p*i <= M:
                ret[p*i] = 0
                i += 1
        p += 1
    return ret

n = int(input())
prime = eratosthenes(n)

dp = [1]*(n+1)

for p in range(len(prime)):
    if p <= 3 or not prime[p]: continue
    for q in range(p//2, p):
        if not prime[q]: continue
        if prime[p-q-1]:
            dp[p] = dp[q]+dp[p-q-1]+1
            break
            
print(dp[n])
