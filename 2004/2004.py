two = [2**i for i in range(1, 31)]
five = [5**i for i in range(1, 14)]

n, k = map(int, input().split())

p2 = 0
p5 = 0

for i in range(len(two)):
    p2 += int(n // two[i])
    p2 -= int(k // two[i]) + int((n-k) // two[i])

for i in range(len(five)):
    p5 += int(n // five[i])
    p5 -= int(k // five[i]) + int((n-k) // five[i])

print(min(p2, p5))

