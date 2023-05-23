def modpow (a, x, p):
    if x == 0:
        return 1
    _t = modpow(a, x//2, p)
    if x % 2 == 1:
        return _t*_t*a % p
    else:
        return _t*_t % p
    
print(modpow(2, int(input())+2, 10**9+7) - 5)
