import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = [0]*n

cnt = 0
for i in range(n): S[i] = input()
for i in range(m):
    if input() in S: cnt += 1
        
print(cnt)
