import sys
input = sys.stdin.readline

s = set()
for i in range(28):
    s.add(int(input()))
    
for k in sorted(list(set([n for n in range(1, 31)]) - s)):
    print(k)
