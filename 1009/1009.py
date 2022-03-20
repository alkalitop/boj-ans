T = int(input())
rest = {
    2: [6, 2, 4, 8],
    3: [1, 3, 9, 7],
    4: [6, 4],
    7: [1, 7, 9, 3],
    8: [6, 8, 4, 2],
    9: [1, 9]
}
for i in range(0, T):
    a, b = map(int, input().split())
    last = a % 10
    if last == 0:
        print(10)
    elif last in [1, 5, 6]:
        print(last)
    elif last in [4, 9]:
        print(rest[last][b % 2])
    else:
        print(rest[last][b % 4])
