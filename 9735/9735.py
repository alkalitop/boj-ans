import sys

input = sys.stdin.readline

n = int(input())

def synthetic_division (a, b, c, x1):
    return [a, a*x1 + b, a*(x1**2) + b*x1 + c]

for _ in range(n):

    a, b, c, d = map(int, input().split())

    x1 = 0
    
    if d != 0:
        for k in range(1, int(abs(d))+1):
            if d % k: continue
            if a*(k**3)+b*(k**2)+c*k+d == 0:
                x1 = k
                break
            elif -a*(k**3)+b*(k**2)-c*k+d == 0:
                x1 = -k
                break
    
    A, B, C = synthetic_division(a, b, c, x1)

    D = B**2 - 4*A*C

    if D > 0:
        x2 = (-B + D**0.5) / (2*A)
        x3 = (-B - D**0.5) / (2*A)
        
        x2 = round(x2, 4) if x2 != 0 else 0
        x3 = round(x3, 4) if x3 != 0 else 0

        print(*map(lambda z: format(z, '.4f'), list(set(sorted([x1, x2, x3])))))

    elif D < 0:
        print(format(x1, '.4f'))

    else:
        x2 = -B / (2*A)

        x2 = round(x2, 4) if x2 != 0 else 0
        
        print(*map(lambda z: format(z, '.4f'), list(set(sorted([x1, x2])))))
