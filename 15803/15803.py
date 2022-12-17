init = lambda : map(int, input().split())
x1, y1 = init()
x2, y2 = init()
x3, y3 = init()

T = 'WHERE IS MY CHICKEN?'
F = 'WINNER WINNER CHICKEN DINNER!'

def solve (P1, P2, P3):
    if P1[0] == P2[0] and P2[0] == P3[0]:
        return T
    if P1[1] == P2[1] and P2[1] == P3[1]:
        return T
    try:
        slope1 = (P2[1]-P1[1])/(P2[0]-P1[0])
        slope2 = (P3[1]-P2[1])/(P3[0]-P2[0])
        if slope1 == slope2:
            return T
    except:
        pass
    return F

print(solve((x1, y1), (x2, y2), (x3, y3)))
    
    
    
    
    
