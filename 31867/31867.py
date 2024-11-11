n = int(input())
s = input()

t = 0
for i in range(n):
    t += 1 if int(s[i]) & 1 else -1
    
if t > 0:
    print(1)
elif t < 0:
    print(0)
else:
    print(-1)
