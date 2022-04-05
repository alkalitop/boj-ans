import math
import sys
input = sys.stdin.readline

p = 1000000007
t = int(input())

for i in range(0, t):
    n, r = map(int, input().split())
    print(math.comb(n, r) % p)
