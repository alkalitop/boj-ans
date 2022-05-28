import math
import sys
input = sys.stdin.readline

def catalan (k):
    return math.comb(2*k, k)//(k+1)

while 1:
    n = int(input())
    if not n: break
    print(catalan(n))
