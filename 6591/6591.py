import math
import sys
input = sys.stdin.readline

while 1:
    n, r = map(int, input().split())
    if not n and not r:
        break
    print(math.comb(n, r))
