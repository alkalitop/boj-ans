def miller_rabin (n, a):
	d = n-1
	r = 0
	while d % 2 == 0:
		d >>= 1
		r += 1
	t = pow(a, d, n)
	if t == 1 or t == n-1:
		return 1
	for i in range(r-1):
		t = pow(t, 2, n)
		if t == n-1:
			return 1
	return 0
	
import sys
input = sys.stdin.readline

cnt = 0

for i in range(int(input())):
	tmp = 0
	s = int(input())
	for a in [2, 3, 5, 7, 11]:
		if miller_rabin(2*s+1, a):
			tmp += 1
		else:
			break
	cnt += tmp // 5
	
