N = int(input())
sol = [0, 3, 5, 6, 8, 9]
val = [0, 3, 4, 1, 4, 1, 2, 5, 2, 3]
a = N%10
if a in sol:
    print((N//10)*2+val[a])
else:
    if N < 10:
        print(-1)
    else:
        print(((N//10)-1)*2+val[a])
