n, r = input().split()
n = int(n)
r = float(r)
c = 0

for k in range(n):
    t = [*map(float, input().split())]
    v = [ complex(t[2*i], t[2*i+1]) for i in range(4) ]
    w = (v[0]+v[2]) / 2
    if r >= abs(w)-abs(w-v[0]): c += 1

print(c)
