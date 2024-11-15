n = int(input())
a = [*map(int, input().split())]
s = 0
r = 0
for g in a:
    s ^= g
for g in a:
    for i in range(1, g+1):
        if s^g^(g-i) == 0:
            r += 1
print(r)
