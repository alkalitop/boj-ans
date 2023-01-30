n, m = map(int, input().split())

d = {}
for i in range(n):
    d[input()] = 1
    
cnt = 0
for i in range(m):
    if d.get(input(), 0): cnt += 1

print(cnt)
