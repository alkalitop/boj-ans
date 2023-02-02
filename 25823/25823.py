M = int(input())
p = 10**9+7

def pow (a, x):
    if x == 0:
        return 1
    t = pow(a, x//2)
    if x % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p

fac = [0]*(2*M+1)
fac[0] = 1

for i in range(1, 2*M+1):
    fac[i] = ((fac[i-1] % p)*(i % p)) % p

res = 0

for n in range(3, M+1):
    u = fac[2*n]
    a = pow(fac[n], 2)
    res += u*pow(a, p-2) % p
    res %= p
    
print(res % p)
