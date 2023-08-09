from math import gcd, log2, floor, sqrt
from random import random

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
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
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

def phi (n):
    res = n
    pr = plr(n, return_dict=1)
    for k in pr:
        res *= k-1
        res //= k
    return res

phisum = [0]*10001
phisum[1] = 1

for i in range(2, 10001):
    phisum[i] = phisum[i-1]+phi(i)
    
for k in range(int(input())):
    n = int(input().split()[1])
    r = 3*phisum[n]-1
    s = f'{r}/2' if r % 2 else r//2
    print(k+1, s)


