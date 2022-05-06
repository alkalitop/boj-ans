move = ((0, 0), (-1, 0), (0, -1), (-1, -1)) # (x, y)

def Z (n, x, y):
    if n == 0: return 0
    m = n >> 1
    q = 0
    if y < m:
        if x >= m:
            q = 1
    else:
        if x < m:
            q = 2
        else:
            q = 3
    t = Z(m, x+move[q][0]*m, y+move[q][1]*m) + q*(m**2)
    return t
	
N, r, c = map(int, input().split())
print(Z(1 << N, c, r))
