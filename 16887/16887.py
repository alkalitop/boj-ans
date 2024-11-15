def g(x):
    if 1 <= x < 4 or 82 <= x < 6724:
        return 0
    elif 4 <= x < 16 or 50626 <= x < 2562991876:
        return 1
    elif 16 <= x < 82 or x >= 2562991876:
        return 2
    else:
        return 3
    
n = int(input())
a = [*map(int, input().split())]
s = 0
for i in range(n):
    s ^= g(a[i])

print('koosaga' if s else 'cubelover')
