base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = input().split()
b = int(b)

ans = 0

for i in range(len(n)):
    ans += int(base.index(n[i]))*(b**(len(n)-i-1))

print(ans)
