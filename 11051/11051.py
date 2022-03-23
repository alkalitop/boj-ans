import math
N, K = map(int, input().split())
print(math.comb(N, K) % 10007)
