def mex(*args):
    for k in range(1001):
        if not k in args:
            return k

g = [0]*1001
g[2] = 1

for i in range(3, 1001):
    a = [0]*(i//2)
    for j in range(i//2):
        a[j] = g[j]^g[i-2-j]
    g[i] = mex(*a)

print(1 if g[int(input())] else 2)        
