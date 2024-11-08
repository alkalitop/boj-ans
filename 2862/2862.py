from bisect import bisect_left

n = int(input())

f = [0]*75
f[1] = 1

for i in range(2, 75):
    f[i] = f[i-1] + f[i-2]

while f[bisect_left(f, n)] != n:
    n -= f[bisect_left(f, n)-1]

print(n)
