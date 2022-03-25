T = int(input())
def keypad (x):
    u = x.lower()
    if u in 'abc':
        return '2'
    elif u in 'def':
        return '3'
    elif u in 'ghi':
        return '4'
    elif u in 'jkl':
        return '5'
    elif u in 'mno':
        return '6'
    elif u in 'pqrs':
        return '7'
    elif u in 'tuv':
        return '8'
    elif u in 'wxyz':
        return '9'

for i in range(0, T):
    inp = input()
    s = ''
    for j in range(0, len(inp)):
        s = s + keypad(inp[j])
    size = len(s)
    if not (size % 2):
        if s[:size//2] == (s[size//2:])[::-1]:
            print('YES')
        else:
            print('NO')
    else:
        if s[:size//2] == (s[size//2+1:])[::-1]:
            print('YES')
        else:
            print('NO')
