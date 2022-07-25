N = input()
c = 0

def func (n):
    d = []
    n = str(n)
    for i in range(0, len(n)-1):
        d.append(int(n[i+1]) - int(n[i]));
    if len(set(d)) == 1:
        return 1
    else:
        return 0
   
for n in range(1, int(N)+1):
    c += 1 if n < 10 else func(n)
print(c)
