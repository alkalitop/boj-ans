from math import log2

def star(k):
    if k == 0:
        return ['*', '* *', '*****']
    else:
        S = star(k-1)
        for i in range(len(S)):
            t1 = 5*(2**(k-1))
            t2 = 2**(k-1)
            space = ' '*(t1+t2-len(S[i]))
            S[i] = S[i] + space + S[i]
        return star(k-1) + S

n = int(log2(int(input())//3))
s = star(n)

for i in range(len(s)):
    t1 = 5*(2**n)
    t2 = 2**n
    space = ' '*((t1+t2-len(s[i]))//2)
    print(space+s[i]+space, end='')
    if i < len(s)-1: print('\n', end='')
