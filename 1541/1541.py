import re

s = list(input())
ops = 0
size = len(s)
for i in range(size):
    if s[i] == '-' and not ops: ops = 1
    if s[i] == '+' and ops: s[i] = '-'
ex = re.sub('\+0+', '+', re.sub('\-0+', '-', re.sub('^0+', '', ''.join(s))))
print(eval(ex))
