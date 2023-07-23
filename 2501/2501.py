n, k = map(int, input().split())
c = 0

for i in range(1, n+1):
    if n % i: continue
    c += 1
    if c == k:
        print(i)
        break

if c < k: print(0)
