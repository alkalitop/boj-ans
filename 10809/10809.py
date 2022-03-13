s = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
pos = [-1]*26
for i in range(0, len(alp)):
	pos[i] = s.find(alp[i])
print(' '.join(map(str, pos)))
