from math import sin, cos

a, b, c = map(int, input().split())

f = lambda x: a*x + b*sin(x) - c
Df = lambda x: a + b*cos(x)

s = c

while abs(f(s)) > 0.0000000001:
    tmp = f(s)/Df(s)
    s -= tmp

print(s)
