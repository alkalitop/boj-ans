import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = [0]*n

for i in range(n):
    S[i] = [0]*n
    num_in = input().split()
    for j in range(n):
        S[i][j] = S[i][j-1] + int(num_in[j]) if j > 0 else int(num_in[0])
			
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
	
    ans = 0
    for i in range(x1-1, x2):
        ans += S[i][y2-1]
        if y1 > 1:
            ans -= S[i][y1-2]
    print(ans)
    
