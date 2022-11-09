input()
A = map(int, input().split())
cnt = 0
for z in A:
    if z == 1:
        continue
    if z == 2:
        cnt += 1
        continue
    isprime = 1
    for i in range(2, z):
        if z % i == 0:
            isprime = 0
            break           
    cnt += isprime
print(cnt)
