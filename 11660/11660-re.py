import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0]*n
s = [0]*n
for i in range(n):
    a[i] = [*map(int, input().split())]
    s[i] = [0]*n
    s[i][0] = a[i][0]
    for j in range(1, n):
        s[i][j] = s[i][j-1] + a[i][j]
    
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    r = 0
    for i in range(x1-1, x2):
        r += s[i][y2-1] - (0 if y1 == 1 else s[i][y1-2])
    print(r)
        
