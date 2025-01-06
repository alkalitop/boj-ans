def sxor(x):
    if x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x+1
    elif x % 4 == 3:
        return 0
    else:
        return x

a, b = map(int, input().split())
print(sxor(b)^sxor(a-1))
