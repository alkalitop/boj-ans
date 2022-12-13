n = int(input())

istart = 1
iend = 1
S = 1

cnt = 1

while iend != n:
    if S == n:
        cnt += 1
    if S > n:
        S -= istart
        istart += 1
    else:
        iend += 1
        S += iend
        
print(cnt)
        
