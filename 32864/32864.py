n = int(input())
a = input().replace(' ', '')
s = [*map(lambda x: len(x), a.split('1'))]
for i in range(len(s)):
    if 0 < i < len(s)-1:
        s[i] += 1
c = 0
i = 0
while i < len(s)-1 and s[i] == 1:
    c += 1
    i += 1
print('alsdkffhgk' if c & 1 else 'mnx')
