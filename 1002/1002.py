import math
T = int(input())
for i in range(0, T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    A = 2*(x2 - x1)
    B = 2*(y2 - y1)
    C = (x1**2 - x2**2) + (y1**2 - y2**2) + (r2**2 - r1**2)
    if A == 0 and B == 0: 
        if r1 == r2 and not (r1 == 0 and r2 == 0):
            print(-1)
        elif r1 == r2 and r1 == 0 and r2 == 0:
            print(1)
        else:
            print(0)
    else:
        d = math.fabs(A*x1 + B*y1 + C) / math.sqrt(A**2 + B**2)
        if d > r1:
            print(0)
        elif d < r1:
            print(2)
        else:
            print(1)
