from math import gcd
seqinput = lambda: map(int, input().split())
n, k = seqinput()
g = gcd(*seqinput(), 360)
for a in [*seqinput()]:
    print('NO' if a % g else 'YES')
