a = []
d = 0

for _ in range(5):
    s = list(input())
    d = max(d, len(s))
    
    a.append(s)
    
for i in range(d):
    r = ''
    for j in range(5):
        if len(a[j]) > i:
            r += a[j][i]
    print(r, end='')

