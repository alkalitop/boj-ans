a, b, c = map(int, input().split())
m = max(a, b, c)
if a+b+c <= m<<1:
    print((a+b+c-m<<1)-1)
else:
    print(a+b+c)
    
