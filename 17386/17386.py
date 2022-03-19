import sys
x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
x3, y3, x4, y4 = map(int, sys.stdin.readline().split(' '))
cont = lambda t, u, v: (u <= t <= v) or (v <= t <= u)
if x1 != x2 and x3 != x4:
    a = (y2-y1)/(x2-x1)
    c = (y4-y3)/(x4-x3)
    b = -a*x1+y1
    d = -c*x3+y3
    if a != c:
        x = (d-b)/(a-c)
        if cont(x, x1, x2) and cont(x, x3, x4):
            if cont(a*x+b, y1, y2) and cont(c*x+d, y3, y4):
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)
else:
    if x1 == x2 and x3 != x4:
        c = (y4-y3)/(x4-x3)
        d = -c*x3+y3
        if cont(x1, x3, x4):
            if cont(c*x1+d, y1, y2):
                print(1)
            else:
                print(0)
        else:
            print(0)
    elif x1 != x2 and x3 == x4:
        a = (y2-y1)/(x2-x1)
        b = -a*x1+y1
        if cont(x3, x1, x2):
            if cont(a*x3+b, y3, y4):
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)
