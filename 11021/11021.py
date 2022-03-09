size = int(input())
for i in range(0, size):
    a, b = map(int, input().split(' '))
    print(f'Case #{i+1}:', a+b)
