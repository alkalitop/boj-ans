import sys
import math
n, k, m = map(int, sys.stdin.readline().split())
size = math.floor(math.log(n, m))
rest = 1
for i in range(0, size): 
    powerbase = m**(size-i)
    m_N = n // powerbase
    n %= powerbase
    m_K = k // powerbase
    k %= powerbase
    rest *= math.comb(m_N, m_K)
rest *= math.comb(n, k)
print(rest % m)
