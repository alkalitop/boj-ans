x = 0
y = 0

A = list(input())
n = len(A)

for i in range(n):
    p = int(A[i])
    if p == 1 or p == 3:
        x += (1 << n-1-i)
    if p == 2 or p == 3:
        y += (1 << n-1-i)

print(n, x, y)
