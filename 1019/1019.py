I = input()

c = [0]*10

A = int(I)
n = len(I)
a = list(map(int, list(I)))


for i in range(1, n+1):
    if a[i-1] > 0:
        for j in range(1, a[i-1]): c[j] += int(10**(n-i))
    if a[i-1] == 0: c[0] -= int(10**(n-i))
    for j in range(10):
        c[j] += (n-i)*int(10**(n-i-1)) * a[i-1]
    c[a[i-1]] += int(I[i:] if i < n else '0')+1
                     
print(*c)
