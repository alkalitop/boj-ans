from math import gcd

def ettinc(M):
    ret = [1]*(M+1)
    ret[0], ret[1] = (0, 0)
    p = 2
    while p <= int(M**0.5):
        if ret[p]:
            ret[p] = 1
            i = 2
            while p*i <= M:
                ret[p*i] = 0
                i += 1
        p += 1
    return ret

n, k, m = map(int, input().split())
prime = ettinc(n)

def legf (n, f):
    for p in range(2, n+1):
        if not prime[p]: continue
        t = p
        while t <= n:
            if not p in f:
                f[p] = 0
            f[p] += n//t
            t *= p

def modpow (a, x, p):
    if x == 0:
        return 1
    t = modpow(a, x//2, p)
    if x & 1:
        return t*t*a % p
    else:
        return t*t % p

nf, kf, uf = {}, {}, {}

legf(n, nf)
legf(k, kf)
legf(n-k, uf)

c = 1

for p in nf:
    c *= modpow(p, nf[p] - kf.get(p, 0) - uf.get(p, 0), m)
    c %= m

print(c)
