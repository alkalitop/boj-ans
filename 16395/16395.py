import sys
import math
n, k = map(int, sys.stdin.readline().split())
print(math.comb(n-1, k-1))
