n, l, r = map(int, input().split())
a = [*map(int, input().split())]
print(int(sorted(a) == (a[:l-1] + sorted(a[l-1:r]) + a[r:])))
