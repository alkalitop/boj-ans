a, b, c = map(int, input().split(' '))
print(a//(c-b)+1 if c-b>0 else -1)
