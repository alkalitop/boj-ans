while 1:
    s = input()
    if s == 'END': break
    t = ''
    for v in reversed(list(s)):
        t += v
    print(t)
