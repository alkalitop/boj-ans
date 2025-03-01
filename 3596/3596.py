def mex(args):
    for k in range(2001):
        if not k in args:
            return k
            
n = int(input())

g = [0]*2001
g[1], g[2], g[3] = 1, 1, 1
g[4], g[5] = 2, 2

if n <= 5:
    print(1)
else:
    for i in range(6, n+1):
        a = [g[i-3], g[i-4], g[i-5]]
        for j in range(1, (i-4)//2+1):
            a.append(g[j]^g[i-j-5])
        g[i] = mex(a)
    print(1 if g[n] else 2)
