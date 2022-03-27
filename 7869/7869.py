import sys
import math
x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())

def angle (a, b, c):
    return 2*math.acos((a*a+b*b-c*c)/(2*a*b))

def sector (r, t):
    return 0.5*(r*r)*t

def triangle (r, t):
    return 0.5*(r*r)*math.sin(t)

def roundf (n):
    g = int(n)
    a = n - g
    if a >= 0.5:
        return g+1
    else:
        return g

d = math.hypot(x2-x1, y2-y1)
A = -1

if d <= abs(r2 - r1) and r1 < r2:
    A = r1*r1*math.pi
elif d <= abs(r2 - r1) and r1 >= r2:
    A = r2*r2*math.pi
elif d > r1+r2:
    A = 0
else:
    t1 = angle(d, r1, r2)
    t2 = angle(d, r2, r1)
    S = sector(r1, t1)+sector(r2, t2)
    T = triangle(r1, t1)+triangle(r2, t2)
    A = S - T

print('%.3f' % float(roundf(A*1000)/1000))
