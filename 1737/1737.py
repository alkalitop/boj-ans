from math import pi

p = {}
def P(n):
    if 0 <= n <= pi: return 1
    if n in p: return p[n]
    p[n] = P(n-1) + P(n-pi)
    return p[n] % 1000000000000000000

print(P(int(input())))
