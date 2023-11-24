import sys
input = sys.stdin.readline

while 1:
    p = input().split()
    if p[0] == '#': break
    if int(p[1]) < 18 and int(p[2]) < 80:
        print(p[0], 'Junior')
    else:
        print(p[0], 'Senior')
    


