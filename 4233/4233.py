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

def is_prime (n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1
   
p, a = map(int, input().split())
while p and a:
    if is_prime(p):
        print('no')
    else:
        if dcpow(a, p) % p == a:
            print('yes')
        else:
            print('no')
    p, a = map(int, input().split())
