n, m = map(int, input().split())
c = 0

for i in range(n):
    if len(input().split('O'))-1 > m//2: c += 1
        
print(c)
