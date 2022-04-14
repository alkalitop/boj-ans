import sys
input = sys.stdin.readline

T = int(input())

def dcpow (a, x, p):
    if x == 0:
        return 1
    t = dcpow(a, x//2, p)
    if x % 2 == 1:
        return t*t*a % p
    else:
        return t*t % p

def facpow (a, n, p):
    if n == 1:
        return a % p
    else:
        res = dcpow(a, 2, p)
        for i in range(3, n+1):
            res = dcpow(res, i, p)
            res %= p
        return res
    
for i in range(T):
    A, N, P = map(int, input().split())
    print('Case #%d: %d' % (i+1, facpow(A, N, P)))
