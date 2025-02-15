s = ''
for i in range(2*int(input())-1):
    t = input()
    s += t if t != '/' else '//'
print(eval(s))
