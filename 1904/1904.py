n = int(input())

p = 1
q = 1
for i in range(n-1):
    p, q = (q%15746, (p+q)%15746)
    
print(q)
