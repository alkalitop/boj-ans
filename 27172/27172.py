n = int(input())
A = list(map(int, input().split()))
B = [None]*(10**6+1)

for x in A:
    B[x] = 0
    
for x in A:
    k = 2
    while x*k <= 10**6:
        if B[x*k] == None:
            k += 1
            continue
        B[x*k] -= 1
        B[x] += 1
        k += 1

S = []

for x in A:
    S.append(B[x])
    
print(*S)

