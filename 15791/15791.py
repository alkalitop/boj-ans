import sys
n, r = map(int, input().split())
p = 1000000007
def dcpow (a, x):
    if x == 0:
        return 1
    t = dcpow(a, x//2)
    if x % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p

def modfac (k):
    t = 1
    for i in range(2, k+1):
        t *= i
        t %= p
    return t

nfac = modfac(n)
a = modfac(r)*modfac(n-r)
print(nfac*dcpow(a, p-2) % p)
