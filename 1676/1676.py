n = int(input())
count = 0
for i in range(1, n+1):
    if not i % 125:
        count += 3
    elif not i % 25:
        count += 2
    elif not i % 5:
        count += 1
print(count)
