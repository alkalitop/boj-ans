import sys
c = 0
M = 0
for i in range(1, 10):
    n = int(sys.stdin.readline())
    if M < n:
        c = i
        M = n
    else:
        pass
print(M)
print(c)
