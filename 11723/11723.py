import sys
input = sys.stdin.readline

S = set()
for _ in range(int(input())):
	inp = input().rstrip()
	cmd, q = (None, None)
	if ' ' in inp:
		cmd, q = inp.split()
	else:
		cmd = inp
	if cmd == 'add':
		S.add(int(q))
	if cmd == 'remove':
		if int(q) in S:
			S.remove(int(q))
	if cmd == 'check':
		print(1 if int(q) in S else 0)
	if cmd == 'toggle':
		if int(q) in S:
			S.remove(int(q))
		else:
			S.add(int(q))
	if cmd == 'all':
		S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
	if cmd == 'empty':
		S = set()
