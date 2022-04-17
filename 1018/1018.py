import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [0]*n
for i in range(n):
    board[i] = input().strip()

count = m*n
for y in range(n-7):
    for x in range(m-7):
        bst, wst = (0, 0)
        for j in range(y, y+8):
            for i in range(x, x+8):
                tile = board[j][i]
                
                if (i+j)%2 == 0: # 시작색이 칠해지는 칸
                    if tile != 'B':
                        bst += 1
                    if tile != 'W':
                        wst += 1
                else: # 시작색이 아닌 색이 칠해지는 칸
                    if tile != 'W':
                        bst += 1
                    if tile != 'B':
                        wst += 1
                            
        count = min(count, bst, wst)
                    
print(count)
