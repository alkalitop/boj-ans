from math import e, log

s, p = map(int, input().split())

if s == p:
    print(1)
else:
    if s/e < log(p):
        print(-1)
    else:
        t = 2
        y0 = -1
        while 1:
            y1 = (s/t)**t
            if y1 < y0:
                print(-1)
                break
            if y1 >= p:
                print(t)
                break
            y0 = y1
            t += 1
                



