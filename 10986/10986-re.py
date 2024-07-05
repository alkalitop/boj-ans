import math
from bisect import *

n, m = map(int, input().split())
a = [*map(int, input().split())]
s = [0]*n
s[0] = a[0] % m

for i in range(1, n):
    s[i] = s[i-1] + a[i]
    s[i] %= m
    
c = 0

for i in range(n):
    if s[i] == 0: c += 1
        
s.sort()        

for k in range(m):
    c += math.comb(bisect_right(s, k) - bisect_left(s, k), 2)
            
print(c)
