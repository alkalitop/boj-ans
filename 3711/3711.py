N = int(input())
for i in range(0, N):
    G = int(input())
    stunum = []
    for j in range(0, G):
        stunum.append(int(input()))
    div = 1
    while G != len(set(map(lambda x: x%div, stunum))):
        div += 1
    print(div)
