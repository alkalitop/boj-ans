n, k = map(int, input().split())
if n == 1:
    print(*([1]*k))
elif n == 2:
    if k == 1:
        print(1, 2)
    else:
        print(-1)
else:
    print(-1)
