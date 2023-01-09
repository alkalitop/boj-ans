a, l = map(int, input().split())
n = 1 + (a - l if a > l else l - a)
print(int(n*(a+l)/2))
