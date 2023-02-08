import sys
input = sys.stdin.readline

p = 10**9+7

def pow (a, x):
    if x == 0:
        return 1
    t = pow(a, x//2)
    if x % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p
        
fac = [0]*(600001)
fac[0] = 1
for i in range(1, 600001):
    fac[i] = ((fac[i-1] % p)*(i % p)) % p

res = 1

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    u = fac[a+b]
    v = fac[a]*fac[b]
    w = (u*pow(v%p, p-2) % p) - 1
    if w < 0:
        w += p
    res *= w
    res %= p
    
print(res % p)
