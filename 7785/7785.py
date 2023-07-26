import sys
input = sys.stdin.readline

s = set()

for _ in range(int(input())):
    a, b = input().split()
    if b == 'enter':
        s.add(a)
    elif b == 'leave':
        s.remove(a)
    
for v in reversed(sorted(list(s))):
    print(v)
