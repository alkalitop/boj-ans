from math import gcd, log2, floor
from random import random
from bisect import bisect_left, bisect_right

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

def rho_seg (n, x, c):
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
		return None
	else:
		if mrpt(d):
			return d
		else:
			return rho_seg(d, x, c)

def plr (n):
    x = 2
    res = [0]*(floor(log2(n))+1)
    i = 0

    while n > 1:
        alternative_c = [-1, 2, -2]
        p = rho_seg(n, x, 1)
        while p == None:
            p = rho_seg(n, x, alternative_c[0])
            del alternative_c[0]
        if p:
            res[i] = p
            i += 1
            n //= p
            if n == 1:
                return res
            if mrpt(n):
                res[i] = n
                return res
        else:
            x = floor((random()*log2(n+1)))+2
    return sorted(res)

def fermat2sq (n):
    seq = list(filter(lambda z: z%4 == 3, plr(n)))
    for t in set(seq):
        if (bisect_right(seq, t) - bisect_left(seq, t)) % 2:
            return 0
    return 1

def legendre3sq (n):
    factor = plr(n)
    e = bisect_right(factor, 2) - bisect_left(factor, 2);
    if e % 2:
        return 1
    else:
        if (n >> e) % 8 == 7:
            return 0
        else:
            return 1