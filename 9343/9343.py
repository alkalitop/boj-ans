import sys
input = sys.stdin.readline

def modmul (a, b, p):
    return ((a%p)*(b%p))%p

def moddivflt (a, b, p):
    return modmul(a, modpow(b, p-2, p), p)

def modpow (a, x, p):
    if x == 0:
        return 1
    _t = modpow(a, x//2, p)
    if x % 2 == 1:
        return _t*_t*a % p
    else:
        return _t*_t % p

fac = [0]*(2*10**6+1)
fac[0] = 1

for i in range(1, 2*10**6+1):
    fac[i] = modmul(fac[i-1], i, 1000000007)
    
def modfact (n, p):
    return fac[n]

def modcombflt (n, k, p):
    _u = modfact(n, p)
    _v = modmul(modfact(k, p), modfact(n-k, p), p)
    return moddivflt(_u, _v, p)

def modcatflt (n, p):
    return moddivflt(modcombflt(modmul(n, 2, p), n, p), n+1, p)

for i in range(int(input())):
    print(modcatflt(int(input()), 1000000007))
