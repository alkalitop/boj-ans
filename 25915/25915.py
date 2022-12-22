dist = lambda a, b: abs(ord(b) - ord(a))
c = input()
r = 0
for s in 'ILOVEYONSEI':
	r += dist(c, s)
	c = s
print(r)
