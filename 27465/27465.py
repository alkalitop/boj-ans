n = int(input())

if n == 1:
    print(4)
elif n == 10**9:
    print(n)
elif n % 2:
    print(n+1)
else:
    print(n+2)
