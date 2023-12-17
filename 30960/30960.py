n = int(input())
a = sorted(list(map(int, input().split())))
b = [(a[i]-a[i-1]) for i in range(1, n)]

b1 = b[::2]
b2 = b[1::2]

d1 = [0]*(n//2)
d1[0] = b1[0]
d2 = [0]*(n//2)
d2[0] = b2[0]

for i in range(1, len(d1)):
    d1[i] = d1[i-1]+b1[i]

for i in range(1, len(d2)):
    d2[i] = d2[i-1]+b2[i]

z = []

for i in range(n-1):
    if i & 1: continue
    z.append(d1[i//2] + (d2[-1]-d2[i//2]) + b[i+1])

print(min(z))
