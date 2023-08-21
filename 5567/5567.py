n = int(input())

T = [0]*n
T[0] = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    if not T[a-1]:
        T[a-1] = []
    T[a-1].append(b-1)
    if not T[b-1]:
        T[b-1] = []
    T[b-1].append(a-1)

S = T[0]

for i in T[0]:
    if T[i]: S = S + T[i]
    
while 0 in S: S.remove(0) 
    
print(len(list(set(S))))
