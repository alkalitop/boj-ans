fac = [1]
r, c, w = map(int, input().split())

for i in range(1, r+w-1):
    fac.append(fac[i-1]*i)

calls = 1
v = 0
for i in range(r-1, r+w-1):
    for j in range(0, calls):
        v += fac[i]//(fac[c+j-1]*fac[i-c-j+1])
    calls += 1
print(v)
