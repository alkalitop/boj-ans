def modadd (a, b, p):
    return ((a%p)+(b%p))%p

def modsub (a, b, p):
    return ((a%p)-(b%p)+p)%p

def modmul (a, b, p):
    return ((a%p)*(b%p))%p

def moddivflt (a, b, p):
    return modmul(a, modpow(b, p-2, p), p)

def modpow (a, x, p):
    if x == 0:
        return 1
    t = modpow(a, x//2, p)
    if x % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p
    
def modfact (n, p):
    t = 1
    for i in range(2, n+1):
        t *= i
        t %= p
    return t

def modcombflt (n, k, p):
    _u = modfact(n, p)
    _v = modmul(modfact(k, p), modfact(n-k, p), p)
    return moddivflt(_u, _v, p)

def modcatflt (n, p):
    return moddivflt(modcombflt(modmul(n, 2, p), n, p), n+1, p)
