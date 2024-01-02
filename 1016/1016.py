from math import ceil

def sol(a, b):
    ret = [1]*(b-a+1)
    p = 2
    while p**2 <= b:
        i = ceil(a//(p**2))
        while (p**2)*i <= b:
            if (p**2)*i >= a:
                ret[(p**2)*i - a] = 0
            i += 1
        p += 1
    return sum(ret)

print(sol(*map(int, input().split())))
