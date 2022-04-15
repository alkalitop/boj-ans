while 1:
    s=input()
    if s=='0':break
    print(['no','yes'][int(s==s[::-1])])
