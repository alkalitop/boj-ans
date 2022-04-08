import sys
import math
input = sys.stdin.readline

scale = 0

cases = int(input())
for i in range(0, cases):
    area = 0
    size = int(input())
    
    init_x = None
    init_y = None
    prev_x = None
    prev_y = None
    
    for n in range(0, size):
        x, y = map(int, input().split())
        if n == 0:
            init_x = x
            init_y = y
            prev_x = x
            prev_y = y
        elif n >= 1:
            area += prev_x*y - x*prev_y
            prev_x = x
            prev_y = y
    
    area += prev_x*init_y - init_x*prev_y
    area = 0.5*abs(area)
    
    scale += area
    
print(math.floor(scale))
