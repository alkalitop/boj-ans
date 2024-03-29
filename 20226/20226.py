from math import gcd, log2, floor, sqrt
from random import random
from bisect import *

def mrpt_seg (n, a):
    d = n-1
    r = 0
    while d % 2 == 0:
        d >>= 1
        r += 1
    t = pow(a, d, n)
    if t == 1 or t == n-1:
        return 1
    for i in range(r-1):
        t = pow(t, 2, n)
        if t == n-1:
            return 1
    return 0

def mrpt (n):
    tmp = 0
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n in prime:
        return 1
    if n % 2 == 0:
        return 0
    for a in prime:
        if not mrpt_seg(n, a):
            return 0
    return 1

def numadd (a, b, p = 0):
    if p == 0:
        return a+b
    return (a+b)%p

def nummul (a, b, p = 0):
    if p == 0:
        return a*b
    return a*b%p

def rho_seg (n, x, c = 1):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 2
    if mrpt(n):
        return n

    y = x
    d = 1

    while d == 1:
        x = numadd(nummul(x, x, n), c, n)
        y = numadd(nummul(y, y, n), c, n)
        y = numadd(nummul(y, y, n), c, n)

        d = gcd(abs(x-y), n)

    if d == n:
        return rho_seg(d, x, -c if c > 0 else -c+1)
    else:
        if mrpt(d):
            return d
        else:
            return rho_seg(d, x)


def plr (n, return_dict = 0):
    x = 2
    if return_dict:
        res = {}
    else:
        res = []
    while n > 1:
        p = rho_seg(n, x)
        if p:
            if return_dict:
                if p in res:
                    res[p] += 1
                else:
                    res[p] = 1
            else:
                res.append(p)
            n //= p
            if n == 1:
                return res
            if mrpt(n):
                if return_dict:
                    if n in res:
                        res[n] += 1
                    else:
                        res[n] = 1
                else:
                    res.append(n)
                return res
        else:
            x = floor((random()*log2(n+1)))+2
    return res
    
def divisor (n):
    res = []
    pr = plr(n, return_dict=1)

    s = ''
    t = []

    i = 0
    for k in pr:
        s += ' '*i + f'for p_{i} in range({pr[k]+1}):\n'
        t.append(f'({k}**p_{i})')
        i += 1

    s += ' '*i + f'if len(t) > 0: res.append({"*".join(t)})'
    exec(s)

    return res

while 1:
    n = int(input())
    if n == 0: break
    if n == 1:
        print(3)
        continue

    ans = 10**45
    div = sorted(divisor(n))

    for i in range(bisect_left(div, n**(1/3)), len(div)):
        k = div[i]
        m = n//k
        
        for j in range(bisect_left(div, m**0.5), len(div)):
            l = div[j]
            if m % l: continue
            s = k + l + m//l
            if ans > s:
                ans = s
            else:
                break
        
    print(ans)
