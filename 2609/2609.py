import math
m, n = map(int, input().split())
G = math.gcd(m, n)
print(G)
print(m*n//G)
