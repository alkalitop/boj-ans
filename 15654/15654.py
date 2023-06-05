n, m = map(int, input().split())

A = sorted(list(map(int, input().split())))

def L1(k):
    s = 'for a_0 in range(n):\n'
    for i in range(1, k):
        s += ' '*i + f'for a_{i} in range(n):\n'
    return s

def L2(k):
    s = ' '*k + 'B = ['
    for i in range(k):
        s += f'A[a_{i}]'
        if i < k-1: s += ', '
    s += ']\n'
    s += ' '*k + 'if len(B) == len(set(B)):\n'
    s += ' '*(k+1) + 'print(*B)'
    return s

exec(L1(m)+L2(m))
