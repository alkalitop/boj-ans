input()
b, s, a = 0, 0, 0

for t in list(input()):
    if t == 'B': b += 1
    if t == 'S': s += 1
    if t == 'A': a += 1

m = max(b, s, a)

if b == s == a:
    print('SCU')
else:
    print(('B' if b == m else '')+('S' if s == m else '')+('A' if a == m else ''))
