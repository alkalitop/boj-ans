def f (n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return f(n-2) + f(n-1)
print(f(int(input())))
