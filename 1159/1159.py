import sys
input = sys.stdin.readline

pre = {}
sel = []
for _ in range(int(input())):
	p = input()[0]
	if not p in pre: pre[p] = 0
	pre[p] += 1
	if pre[p] == 5: sel.append(p)

if len(sel):
	print(''.join(sorted(sel)))
else:
	print('PREDAJA')
