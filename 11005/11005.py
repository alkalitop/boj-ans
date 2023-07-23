from math import log

base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = map(int, input().split())

ans = ''

r = int(log(n, b))

for i in range(r):
    d = b**(r - i)
    ans += base[n//d]
    n %= d

ans += base[n]

print(ans)
