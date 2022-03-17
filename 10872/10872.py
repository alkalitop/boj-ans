def fact(n):
    if n*(n-1) == 0:
        return 1
    return n*fact(n-1)
print(fact(int(input())))
