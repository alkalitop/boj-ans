from collections import deque

n, m = map(int, input().split())
A = list(map(int, input().split()))

deq = deque()

for i in range(n):
	while len(deq) > 0 and deq[-1][0] > -A[i]:
		deq.pop()
	deq.append((-A[i], i))
	if deq[0][1] <= i-2*m+1:
		deq.popleft()
	if 2*m-2 <= i:
		print(-deq[0][0])
