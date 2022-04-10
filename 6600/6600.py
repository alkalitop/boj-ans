import sys
import math
input = sys.stdin.readline

pi = 3.141592653589793

while 1:
    line = input()
    if not line:
        break
    x1, y1, x2, y2, x3, y3 = map(float, line.split())
    a = math.hypot(x2-x1, y2-y1)
    b = math.hypot(x3-x2, y3-y2)
    c = math.hypot(x1-x3, y1-y3)
    C = math.acos((a**2+b**2-c**2)/(2*a*b))
    r = c/(math.sin(C)*2)
    print('%.2f' % (2*pi*r))
