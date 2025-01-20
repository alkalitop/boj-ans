x, y = map(int, input().split())
if x < y: x, y = y, x

if x & 1:
    t = -~y & 1
else:
    p, q = x-y, 2
    while-~x&1:x>>=1;q*=2
    t = min(p % q, 1)
    
print('BA'[t], 'player wins')
