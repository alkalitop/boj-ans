import sys
input = sys.stdin.readline

M = 10**6

divsum = [1]*(M+1)

for i in range(2, M+1):
    j = 1
    while i*j <= M:
        divsum[i*j] += i
        j += 1
        
S = [0]*(M+1)
S[1] = 1
for i in range(2, M+1):
    S[i] = S[i-1] + divsum[i]
    
for _ in range(int(input())):
    print(S[int(input())])
