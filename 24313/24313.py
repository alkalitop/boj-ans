a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

k = c-a1

if a0 <= 0:
    print(0 if k < 0 else 1)
else:
    if k > 0:
        print(0 if a0 > k*n0 else 1)
    else:
        print(0)
