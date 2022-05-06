import sys
from bisect import bisect_left
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [0]*n
for i in range(n):
	coin[i] = int(input())

cnt = 0
rest = k
while rest > 0:
	L = rest if rest in coin else coin[bisect_left(coin, rest)-1]
	cnt += rest // L
	rest %= L
	
print(cnt)
