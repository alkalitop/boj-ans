import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = set()
B = set()

for _ in range(n):
	A.add(input())
	
for _ in range(m):
	B.add(input())

C = A & B
print(len(C))
for v in sorted(list(C)):
	print(v.rstrip())
