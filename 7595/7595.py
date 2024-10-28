import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if not n: break
    for i in range(n):
        print('*'*(i+1))
