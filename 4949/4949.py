while 1:
    s = input()
    if s == '.': break
    
    b = []
    for i in range(len(s)):
        if s[i] == '(':
            b.append(0)
        if s[i] == ')':
            if len(b) and b[-1] == 0:
                del b[-1]
            else:
                print('no')
                break
        if s[i] == '[':
            b.append(1)
        if s[i] == ']':
            if len(b) and b[-1] == 1:
                del b[-1]
            else:
                print('no')
                break
        if s[i] == '.':
            if len(b) == 0:
                print('yes')
            else:
                print('no')


