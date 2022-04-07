import math
n, k = map(int, input().split())
H = lambda x, y: math.comb(x+y-1, y)
print(H(k, n) % 1000000000)
