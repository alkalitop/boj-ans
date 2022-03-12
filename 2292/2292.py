n = int(input())
acc, c = [1, 1]
while n > acc:
    acc += 6*c
    c += 1
print(c)
