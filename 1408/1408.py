h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
h = h2 - h1
m = m2 - m1
s = s2 - s1
if s < 0:
    s += 60
    m -= 1
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24
pad = lambda x: x if len(x) == 2 else '0' + x
print('{0}:{1}:{2}'.format(pad(str(h)), pad(str(m)), pad(str(s))))
