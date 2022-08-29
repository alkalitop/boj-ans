s = input()
isword = 0
c = 0
for i in range(len(s)):
    if s[i] == ' ':
        isword = 0
    else:
        if isword == 0:
            c += 1
            isword = 1
        else:
            pass
print(c)
