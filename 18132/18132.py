import math
import sys
input = sys.stdin.readline

def catalan (k):
    return math.comb(2*k, k)//(k+1)

for i in range(int(input())):
    print(catalan(int(input())+1) % 1000000007)
