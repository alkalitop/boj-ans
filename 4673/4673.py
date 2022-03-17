import math

nums = set()
def gen (x):
    linesum = 0
    for i in range(0, math.floor(math.log10(x))+1):
        linesum += int(str(x)[i])
    if x + linesum <= 10000:
        nums.add(x + linesum)

for i in range(1, 10001):
    gen(i)

for i in range(1, 10001):
    if not (i in nums):
        print(i)
