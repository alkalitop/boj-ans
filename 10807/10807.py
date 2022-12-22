input()
A = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in A:
    if i == v:
        cnt += 1
print(cnt)
        
