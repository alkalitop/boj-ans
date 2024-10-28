import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = [0]*100
c = 0
for _ in range(n):
    r_len, r_vel = map(int, input().split())
    for i in range(c, c+r_len):
        s[i] += r_vel
    c += r_len

c = 0
for _ in range(m):
    r_len, r_vel = map(int, input().split())
    for i in range(c, c+r_len):
        s[i] = max(r_vel - s[i], 0)
    c += r_len

print(max(s))
