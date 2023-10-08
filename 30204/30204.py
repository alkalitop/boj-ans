x = int(input().split()[1])
if sum(list(map(int, input().split()))) % x:
    print(0)
else:
    print(1)

