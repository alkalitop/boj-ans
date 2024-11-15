def g(x):
    if x % 4:
        if x % 4 == 3:
            return x+1
        else:
            return x
    else:
        return x-1
    
n = int(input())
a = [*map(int, input().split())]
s = g(a[0])

for i in range(1, n):
    s ^= g(a[i])
    
print('koosaga' if s else 'cubelover')
