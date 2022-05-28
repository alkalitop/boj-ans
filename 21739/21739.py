import math

def catalan (k):
    return math.comb(2*k, k)//(k+1)

print(catalan(int(input())) % 1000000007)
