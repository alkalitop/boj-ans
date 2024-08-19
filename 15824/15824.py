n = int(input())
s = sorted([*map(int, input().split())])
m = 10**9+7

r = 0
for i in range(n):
    t = (pow(2, i, m) - pow(2, n-i-1, m))
    r += (s[i]*t) % m
    r %= m
print(r)
        
