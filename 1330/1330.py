a, b = map(int, input().split(' '))
d = a-b
print('==' if d==0 else ('<' if d<0 else '>'))
