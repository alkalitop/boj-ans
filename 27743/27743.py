n, m = map(int, input().split())
d = 10**9+7

if m == 1:
    print(pow(2, n, d) - 1)
else:
    t = m*pow(2, n+1, d) - 2*m - 1
    print(t % d)
