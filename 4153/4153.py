a, b, c = map(int, input().split(' '))
h2 = lambda x,y: x**2+y**2
while a != 0:
    if h2(a,b) == c**2 or h2(b,c) == a**2 or h2(c,a) == b**2:
	print('right')
	a, b, c = map(int, input().split())
    else:
	print('wrong')
	a, b, c = map(int, input().split())
