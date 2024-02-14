n = int(input())
liq = sorted([*map(int, input().split())])
ans = liq[:3]
s = abs(sum(ans))

for i in range(n):
    p = liq[i]
    x, y = 0, n-1
    while x < y:
        if x == i:
            x += 1
            continue
        if y == i:
            y -= 1
            continue
        q, r = liq[x], liq[y]
        t = p+q+r
        if abs(t) < s:
            ans = [p, q, r]
            s = abs(t)
        if t > 0:
            y -= 1
        else:
            x += 1

print(*ans)
