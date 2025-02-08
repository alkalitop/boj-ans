t = input()
s = input()

for i in range(len(s)):
    if s in t:
        print('yes')
        break
    s = s[1:] + s[0]
else:
    print('no')
