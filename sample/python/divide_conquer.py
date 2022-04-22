def dcpow (a, n, p):
    if n == 0:
        return 1
    t = dcpow(a, n//2)
    if n % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p

def modfac (n):
    t = 1
    for i in range(2, n+1):
        t *= i
        t %= p
    return t
