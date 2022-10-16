from math import gcd, log2, floor
from random import random
from decimal import *

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

def rho_seg (n, x):
	if n == 1:
		return 0
	if n % 2 == 0:
		return 2
	if mrpt(n):
		return n
		
	y = x
	d = 1
	
	while d == 1:
		x = numadd(nummul(x, x, n), 1, n)
		y = numadd(nummul(y, y, n), 1, n)
		y = numadd(nummul(y, y, n), 1, n)
		
		d = gcd(abs(x-y), n)
		
	if d == n:
		return rho_seg2(d, x)
	else:
		if mrpt(d):
			return d
		else:
			return rho_seg(d, x)
			
def rho_seg2 (n, x):
	if n == 1:
		return 0
	if n % 2 == 0:
		return 2
	if mrpt(n):
		return n
		
	y = x
	d = 1
	
	while d == 1:
		x = numadd(nummul(x, x, n), -1, n)
		y = numadd(nummul(y, y, n), -1, n)
		y = numadd(nummul(y, y, n), -1, n)
		
		d = gcd(abs(x-y), n)
		
	if d == n:
		return rho_seg3(d, x)
	else:
		if mrpt(d):
			return d
		else:
			return rho_seg2(d, x)
			
def rho_seg3 (n, x):
	if n == 1:
		return 1
	if n % 2 == 0:
		return 2
	if mrpt(n):
		return n
		
	y = x
	d = 1
	
	while d == 1:
		x = numadd(nummul(x, x, n), 2, n)
		y = numadd(nummul(y, y, n), 2, n)
		y = numadd(nummul(y, y, n), 2, n)
		
		d = gcd(abs(x-y), n)
		
	if d == n:
		return 0
	else:
		if mrpt(d):
			return d
		else:
			return rho_seg3(d, x)

def plr (n):
	x = 2
	res = []
	i = 0
	while n > 1:
		p = rho_seg(n, x)
		if p:
			res.append(p)
			i += 1
			n //= p
			if n == 1:
				return res
			if mrpt(n):
				res.append(n)
				return res
		else:
			x = floor((random()*log2(n+1)))+2
	return res

n = int(input())

if n == 1:
	print(1)
else:
	factor = list(set(plr(n)))
	n = Decimal(n)
	for i in factor:
		n *= Decimal(i-1)/Decimal(i)
	print(round(n))
