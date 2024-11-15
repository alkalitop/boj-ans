def g(x):
    return x+1>>1 if x & 1 else x-1>>1
    
n = int(input())
a = [*map(int, input().split())]
s = g(a[0])

for i in range(1, n):
    s ^= g(a[i])
    
print('koosaga' if s else 'cubelover')
