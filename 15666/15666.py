from bisect import *
rb = bisect_right
lb = bisect_left

n, m = map(int, input().split())

A = sorted(list(map(int, input().split())))

prev = [-1]*m

def L1(k):
    s = 'for a_0 in range(n):\n'
    s += ' ' + f'if prev[0] == A[a_0]: continue\n'
    for i in range(1, k):
        s += ' '*i + f'for a_{i} in range(a_{i-1}, n):\n'
        s += ' '*(i+1) + f'if prev[{i}] == A[a_{i}]: continue\n'
    return s

def L2(k):
    s = ' '*k + 'B = ['
    for i in range(k):
        s += f'A[a_{i}]'
        if i < k-1: s += ', '
    s += ']\n'
    s += ' '*(k) + 'print(*B)\n'
    return s
    
def L3(k):
    s = ''
    for i in range(k):
        for j in range(i+1):
            if 0 <= j < i:
                s += ' '*(m-i) + f'prev[{m-j-1}] = -1\n' 
            else:
                s += ' '*(m-i) + f'prev[{m-j-1}] = A[a_{m-j-1}]\n' 
    return s
    
exec(L1(m)+L2(m)+L3(m))
