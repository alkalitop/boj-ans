d = 10**9+7

def modadd (a, b):
    return ((a%d)+(b%d))%d

def modsub (a, b):
    return ((a%d)-(b%d))%d

def modmul (a, b):
    return ((a%d)*(b%d))%d

def moddivflt (a, b):
    return modmul(a, modpow(b, d-2))

def modpow (a, x):
    if x == 0:
        return 1
    _t = modpow(a, x//2)
    if x % 2 == 1:
        return _t*_t*a % d
    else:
        return _t*_t % d
       
n, p = map(int, input().split())

fac = [1]*(p+2)
facinv = [1]*(p+2)

for i in range(1, p+2):
    fac[i] = modmul(fac[i-1], i)
    facinv[i] = modpow(fac[i], d-2)
    
def modcombflt (n, k):
    return modmul(modmul(fac[n], facinv[k]), facinv[n-k])
    
dp = [0]*(p+1)

dp[0] = n
c = modpow(n+1, 2)

for i in range(1, p+1):
    dp[i] = c-1
    c = modmul(c, n+1)
    for j in range(2, i+2):
        dp[i] -= modmul(modcombflt(i+1, j), dp[i+1-j])
        dp[i] %= d
    dp[i] = moddivflt(dp[i], i+1)
    
print(dp[p])
