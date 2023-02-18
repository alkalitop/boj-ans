from math import log2

def pow (a, x):
    if x == 0:
        return 1
    _t = pow(a, x//2)
    if x % 2 == 1:
        return _t*_t*a
    else:
        return _t*_t

n = int(input())
r = n
c = 0

ans = 0
while r > 0:
    t = int(log2(r))
    r -= pow(2, t)
    ans += pow(2, c) * pow(3, t)
    c += 1
    
print(ans)
