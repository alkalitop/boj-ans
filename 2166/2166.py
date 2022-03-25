u = 0
size = int(input())
prevX = None
prevY = None
initX = None
initY = None
for n in range(0, size):
    x, y = map(int, input().split())
    if n == 0:
        initX = x
        initY = y
        prevX = x
        prevY = y
    elif n >= 1:
        u += prevX*y - x*prevY
        prevX = x
        prevY = y
u += prevX*initY - initX*prevY
print(0.5*abs(u))
