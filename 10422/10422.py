import sys
from math import comb

input = sys.stdin.readline

def catalan (n):
    return comb(2*n, n)//(n+1)

for i in range(int(input())):
    t = int(input())
    if t % 2:
        print(0)
    else:
        print(catalan(t//2) % 1000000007)
