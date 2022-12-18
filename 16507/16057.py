import sys
input = sys.stdin.readline

c, r, q = map(int, input().split())
S = [0]*c

for i in range(c):
    S[i] = [0]*r
    num_in = input().split()
    for j in range(r):
        S[i][j] = S[i][j-1] + int(num_in[j]) if j > 0 else int(num_in[0])	
							
for _ in range(q):
    c1, r1, c2, r2 = map(int, input().split())
	
    tot = 0
    for i in range(c1-1, c2):
        tot += S[i][r2 - 1]
        if r1 > 1:
            tot -= S[i][r1 - 2]
    size = (r2-r1+1)*(c2-c1+1)
    print(tot // size)
    
