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

m = int(input())
result = 0
for i in range(0, m):
    n, s = map(int, input().split())
    result += s*dcpow(n, p-2) % p

print(result % p)
