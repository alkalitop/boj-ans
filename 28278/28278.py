import sys
input = sys.stdin.readline

n = int(input())
stk = []

for i in range(n):
    s = input()
    if s[0] == '1':
        k = int(s.split()[1])
        stk.append(k)
        continue
    s = int(s)
    if s == 2:
        if len(stk):
            print(stk.pop())
        else:
            print(-1)
    if s == 3:
        print(len(stk))
    if s == 4:
        print(0 if len(stk) else 1)
    if s == 5:
        if len(stk):
            print(stk[-1])
        else:
            print(-1)
