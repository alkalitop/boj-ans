import sys
from math import gcd
input = sys.stdin.readline

n, b = map(int, input().split())
sum_x = 0
sum_y = 0

for i in range(n):
    x, y = map(int, input().split())
    sum_x += x
    sum_y += y
    
if sum_x == 0:
    print('EZPZ')
else:
    p = sum_x
    q = sum_y - n*b
    if q % p == 0:
        print(q // p)
    else:
        g = gcd(abs(p), abs(q))
        p = p//g
        q = q//g
        if p > 0:
            print(str(q)+'/'+str(p))
        elif p < 0:
            print(str(-q)+'/'+str(-p))
        
    
