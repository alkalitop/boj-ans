from math import log10
import sys

def sol(s):
    cpx, *v = s.split()
    v = [*map(int, v)]
    r = 8 + log10(v[2]) - log10(v[1])
    u = log10(v[0])
    if cpx == 'O(N^2)':
        u *= 2
    elif cpx == 'O(N^3)':
        u *= 3
    elif cpx == 'O(N!)':
        u = sum([log10(i+1) for i in range(v[0])])
    elif cpx == 'O(2^N)':
        u = v[0]*log10(2)
    return u <= r

input = sys.stdin.readline

for _ in range(int(input())):
    print('May Pass.' if sol(input()) else 'TLE!')
