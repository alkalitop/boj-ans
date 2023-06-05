n, m = map(int, input().split())

A = [1, 2, 3, 4, 5, 6, 7, 8][:n]
loop = []
C = 1

def L1(k):
    s = 'for a_0 in range(n-m+1):\n'
    for i in range(1, k):
        s += ' '*i + f'for a_{i} in range(a_{i-1}+1, n-m+{i+1}):\n'
    return s

def L2(k):
    s = ' '*k + 'B = ['
    for i in range(k):
        s += f'A[a_{i}]'
        if i < k-1: s += ', '
    s += ']\n'
    s += ' '*k + 'print(*B)'
    return s

exec(L1(m)+L2(m))
