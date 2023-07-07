from bisect import *
n = int(input().split()[0])
a = list(map(int, input().split()))

c = n**2

l = a[:n]
r = sorted(a[n:])

for i in l:
    c -= bisect_right(r, i) - bisect_left(r, i)   
print(c)
