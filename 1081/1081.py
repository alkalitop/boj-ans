def digitcount(x):
    if x < 0: return [0]
    
    x = str(x)
    
    c = [0]*10
    n = len(x)
    a = list(map(int, list(x)))

    for i in range(1, n+1):
        if a[i-1]:
            for j in range(1, a[i-1]): c[j] += int(10**(n-i))
        else: c[0] -= int(10**(n-i))
        for j in range(10):
            c[j] += (n-i)*int(10**(~-n-i)) * a[~-i]
        c[a[i-1]] += int(x[i:] if i < n else '0')+1
                     
    return c
    
L, U = map(int, input().split())
print(sum([v[0]*v[1] for v in list(enumerate(digitcount(U)))])-sum([v[0]*v[1] for v in list(enumerate(digitcount(L-1)))]))
