def fact5 (n):
    res = 1
    for i in range(2, n+1):
        res *= i
        while not res % 10:
            res //= 10
        res %= 10**13
    return str(res % 100000).rjust(5, '0')

print(fact5(int(input())))
