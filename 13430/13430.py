p = 10**9+7

def pow (a, x):
    if x == 0:
        return 1
    t = pow(a, x//2)
    if x % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p

        
k, n = map(int, input().split())
     
fac = [0]*(k+2)
fac[0] = 1
for i in range(1, k+2):
    fac[i] = ((fac[i-1] % p)*(i % p)) % p

res = 1

for j in range(k+1):
    res *= n+j
    res %= p
    
res *= pow(fac[k+1], p-2)
res %= p

print(res)
