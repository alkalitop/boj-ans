a, b, c, d, e, f = map(int, input().split())

s1 = lambda x, y: a*x + b*y == c
s2 = lambda x, y: d*x + e*y == f

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if s1(i, j) and s2(i, j):
            print(i, j)
            break
