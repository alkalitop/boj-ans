z = 3*(10**6)+1

def mex(*args):
    for k in range(z):
        if not k in args:
            return k

f = [0]*33
f[1] = 1

for i in range(2, 33):
    f[i] = f[i-1] + f[i-2]
    
g = [0]*z
g[1] = 1
g[2] = 2
g[3] = 3

for i in range(4, z):
    a = []
    for j in range(1, 33):
        if f[j] > i:
            break
        a.append(g[i-f[j]])
    g[i] = mex(*a)

n = int(input())
p = [*map(int, input().split())]
s = g[p[0]]
for i in range(1, n):
    s ^= g[p[i]]

print('koosaga' if s else 'cubelover')        
