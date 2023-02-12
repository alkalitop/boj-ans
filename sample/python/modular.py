def modadd (a, b, p):
    return ((a%p)+(b%p))%p

def modsub (a, b, p):
    return ((a%p)-(b%p))%p

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
    
def modfact (n, p):
    _t = 1
    for i in range(2, n+1):
        _t *= i
        _t %= p
    return _t

def modcombflt (n, k, p):
    _u = modfact(n, p)
    _v = modmul(modfact(k, p), modfact(n-k, p), p)
    return moddivflt(_u, _v, p)
