import math

def catalan (k):
    return math.comb(2*k, k)//(k+1)

d, m = map(int, input().split())

print(catalan(d//2-1) % m)

