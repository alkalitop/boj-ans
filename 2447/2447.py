n = int(input())

plot = [1]*n
for i in range(n):
    plot[i] = [1]*n

def star (m, x=0, y=0):
    if m == 3:
        plot[x+1][y+1] = 0
        return 0
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    for u in range(x+m//3, x+2*(m//3)):
                        for v in range(y+m//3, y+2*(m//3)):
                            plot[u][v] = 0
                else:
                    star(m//3, x+i*(m//3), y+j*(m//3))

star(n)
for i in range(n):
    for j in range(n):
        print((' ', '*')[plot[i][j]], end=('' if j < n-1 else '\n'))
