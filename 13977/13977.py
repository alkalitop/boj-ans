import sys
import math

input = sys.stdin.readline

p = 1000000007
def dcpow (a, x):
    if x == 0:
        return 1
    t = dcpow(a, x//2)
    if x % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p

modfac = [1]*4000001
for i in range(1, 4000001):
    modfac[i] = modfac[i-1]*i % p

m = int(input())
for i in range(0, m):
    n, r = map(int, input().split())
   
    nfac = modfac[n]
    a = modfac[r]*modfac[n-r]
    print(nfac*dcpow(a, p-2) % p)
