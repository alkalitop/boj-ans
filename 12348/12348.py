s = input()
n = int(s)

if n < 100:
    for i in range(n+1):
        if i+sum(list(map(int, str(i)))) == n:
            print(i)
            break
        if i == n:
            print(0)
else:
    for i in range(9*len(s), 0, -1):
        if sum(list(map(int, str(n-i)))) == i:
            print(n-i)
            break
        if i == 1:
            print(0)
