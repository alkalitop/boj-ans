n = int(input())
s = [*map(int, input().split())]
t = s[0]
for i in range(1, n):
    t ^= s[i]
if t:
    print('koosaga')
else:
    print('cubelover')
