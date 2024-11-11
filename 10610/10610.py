s = [*map(int, list(input()))]

if not(0 in s) or sum(s) % 3:
    print(-1)
else:
    print(''.join([*map(str, sorted(s, reverse=1))]))
