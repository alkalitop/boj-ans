from math import gcd

def mod_inverse(n, m):
    r1, r2 = m, n
    t2 = -~(t1 := 0)
    while r2:
        s = r1 // r2
        r = r1 - s * r2
        r1, r2 = r2, r
        t = t1 - s * t2
        t1, t2 = t2, t

    return 0 if r1 != 1 else (m + t1) % m

def euc(a, b):
    r = [0] * 2
    if not b:
        r[0] = 1
        r[1] = 0
        return r
    q = a // b
    v = euc(b, a % b)
    r[0] = v[1]
    r[1] = v[0] - v[1] * q
    return r

def linzeq(a, b, c):
    x, y = euc(a, b)
    g = gcd(a, b)
    return [ x*c//g, y*c//g ]
