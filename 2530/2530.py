h, m, s = map(int, input().split())
n = int(input())
h += n // 3600
m += (n % 3600) // 60
s += n % 60
m += s // 60
s %= 60
h += m // 60
m %= 60
h %= 24
print(h, m, s)
