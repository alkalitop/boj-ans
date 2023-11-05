from math import gcd

def mrpt_seg (n, a):
    d = ~-n
    r = 0
    while -~n & 1:
        d >>= 1
        r += 1
    t = pow(a, d, n)
    if t == 1 or t == ~-n:
        return 1
    for i in range(~-r):
        t = pow(t, 2, n)
        if t == ~-n:
            return 1
    return 0
	
def mrpt (n):
    tmp = 0
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n in prime:
        return 1
    if -~n & 1:
        return 0
    for a in prime:
        if not mrpt_seg(n, a):
            return 0
    return 1

def numadd (a, b, m = 0):
    if not m:
        return a+b
    return (a+b) % m

def nummul (a, b, m = 0):
    if not m:
        return a*b
    return ((a%m) * (b%m)) % m

def rho_seg (n, x, c = 1):
    if n == 1:
        return 0
    if -~n & 1:
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

div = {}
ds = 0

def plr (n):
    x = 2
    global ds
    while n > 1:
        p = rho_seg(n, x)
        if p:
            if not p in div:
                div[p] = 0
            div[p] += 1
            ds = max(ds, div[p])
            n //= p
            if n == 1:
                return 0
            if mrpt(n):
                if not n in div:
                    div[n] = 0
                div[n] += 1
                ds = max(ds, div[n])
                return 0
        else:
            x = 0
    return 0

input()
for a in list(map(int, input().split())):
    plr(a)

ans = 0

for t in div:
    if div[t] == ds:
        ans += 1

print(ds)
print(~-(1<<ans))
