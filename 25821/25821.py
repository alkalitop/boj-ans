import re
r1 = re.compile('^0+')
r2 = re.compile('0+$')

def mrpt_seg (n, a):
    d = n-1
    r = 0
    while d % 2 == 0:
        d >>= 1
        r += 1
    t = pow(a, d, n)
    if t == 1 or t == n-1:
        return 1
    for i in range(r-1):
        t = pow(t, 2, n)
        if t == n-1:
            return 1
    return 0

def mrpt (n):
    tmp = 0
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n in prime:
        return 1
    if n % 2 == 0:
        return 0
    for a in prime:
        if not mrpt_seg(n, a):
            return 0
    return 1

c = [2, 3, 5, 7, 11]

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        s = str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(m)+str(l)+str(k)+str(j)+str(i)
                        s = re.sub(r1, '', s)
                        s = re.sub(r2, '', s)
                        if s=='': continue
                        s = int(s)
                        if s > 100 and mrpt(s):
                            c.append(s)
                            
from bisect import *
a, b = map(int, input().split())

print(bisect_right(c, b) - bisect_left(c, a))
