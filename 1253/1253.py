from bisect import bisect_right

bsr = bisect_right

n = int(input())

A = list(map(int, input().split()))
A.sort()

k = 0

cnt = 0
while k < n:
    m = A[k] # 두 수 합 서치할 수
    last_m = bsr(A, m) # 젤 오른쪽에 있는 m 인덱스
    amt_m = last_m - k # m 개수
    
    i = 0
    j = n-1

    while j-i > 0:

        if i == k:
            i += 1
        if j == k:
            j -= 1
        if j-i < 1:
            break

        p = A[i]
        q = A[j]

        if p+q < m:
            i += 1
        elif p+q > m:
            j -= 1
        else:
            cnt += amt_m
            break

    k = last_m

print(cnt)
