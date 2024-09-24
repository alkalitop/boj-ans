import sys
input = sys.stdin.readline

for i in range(int(input())):
    s = [*map(int, input().split())]
    n = s[0]
    s = s[1:]
    d = s[1] - s[0]
    t = ', '.join([*map(str, s)])
    for i in range(2, n):
        if s[i] - s[i-1] != d:
            print(f'The sequence [{t}] is not an arithmetic sequence.')
            break
    else:
        u = ', '.join([str(s[-1] + (i+1)*d) for i in range(5)])
        print(f'The next 5 numbers after [{t}] are: [{u}]')
