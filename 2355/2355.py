a, l = map(int, input().split())
n = a - l + 1 if a > l else l - a + 1
print(int(n*(a+l)/2))
