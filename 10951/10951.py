import sys

inp = sys.stdin.readline()
while inp != '':
	a, b = map(int, inp.split(' '))
	print(a+b)
	inp = sys.stdin.readline()
