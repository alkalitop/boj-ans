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
			return rho_seg(d, x)

def plr (n):
    x = 2
    res = [0]*(floor(log2(n))+1)
    i = 0

    while n > 1:
        alternative_c = [-1, 2, -2, 3, -3, 4, -4, 5, -5]
        p = rho_seg(n, x, 1)
        while p == None:
            p = rho_seg(n, x, alternative_c[0])
            del alternative_c[0]
        if p:
            res[i] = p
            i += 1
            n //= p
            if n == 1:
                return sorted(res)
            if mrpt(n):
                res[i] = n
                return sorted(res)
        else:
            x = floor((random()*log2(n+1)))+2
    return sorted(res)

F = [None]*93
F[0] = 0
F[1] = 1

for i in range(2, 93):
    F[i] = F[i-1] + F[i-2]
    
while 1:
    try:
        inp = input()
        if inp.strip() == '':
            break
    
        lo, hi = map(lambda z: int(z, base=16), inp.split())
        if lo >= hi:
            break
    
        istart = bisect_left(F, lo);
        iend = bisect_right(F, hi);
        print(f'Range {lo} to {hi}:')

        if istart == iend:
            print('No Fibonacci numbers in the range')
            print()
            continue
        
    
        for i in range(istart, iend):
            lg = None
            pr = None
            if i == 0:
                lg = 'lg does not exist'
                pr = 'No prime factors'
            elif i == 1 or i == 2:
                lg = 'lg is 0.000000'
                pr = 'No prime factors'
            else:
                primestr = ''
                for p in plr(F[i]):
                    if not p:
                        continue
                    primestr += str(p) + ' '
                lg = f'lg is {log2(F[i]):.6f}'
                pr = f'Prime factors: {primestr}'
            print(f'Fib({i}) = {F[i]}, {lg}')
            print(pr)

        print()
    except EOFError:
        break
        
