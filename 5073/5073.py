while 1:
    a, b, c = map(int, input().split())
    if not a: break
    m = max(a, b, c)
    if a+b+c <= m<<1:
        print('Invalid')
    else:
        if (a-b)*(b-c)*(c-a):
            print('Scalene')
        else:
            if a == b == c:
                print('Equilateral')
            else:
                print('Isosceles')
