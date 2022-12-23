n = int(input())
m = int(input())

A = list(map(int, input().split()))
A.sort()

i = 0
j = n-1

cnt = 0
while j-i > 0:
    p = A[i]
    q = A[j]
    if p+q < m:
        i += 1
    elif p+q > m:
        j -= 1
    else:
        cnt += 1
        j -= 1

print(cnt)
