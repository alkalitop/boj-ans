T = int(input())
dist2 = lambda x, y, p, q: (x-p)**2 + (y-q)**2
for i in range(0, T):
    count = 0
    x1, y1, x2, y2 = map(int, input().split(' '))
    p = int(input())
    for j in range(0, p):
        cx, cy, r = map(int, input().split(' '))
        cond1 = dist2(x1, y1, cx, cy) <= r**2
        cond2 = dist2(x2, y2, cx, cy) <= r**2
        if cond1 and (not cond2):
            count += 1
        elif (not cond1) and cond2:
            count += 1
    print(count)
