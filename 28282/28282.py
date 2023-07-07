from bisect import bisect_left, bisect_right

x, k = map(int, input().split())
a = list(map(int, input().split()))

r = x**2

left = a[:x]
right = sorted(a[x:])

for i in left:
    r -= bisect_right(right, i) - bisect_left(right, i)
    
print(r)
