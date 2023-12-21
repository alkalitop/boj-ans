c = 0

s = set()

for i in range(int(input())):
    t = input()
    if t == 'ENTER':
        c += len(s)
        s = set()
    else:
        s.add(t)

c += len(s)        
print(c)
