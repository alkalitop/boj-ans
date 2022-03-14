tc = int(input())
for i in range(0, tc):
    result = ''
    n, s = input().split(' ')
    n = int(n)
    for j in range(0, len(s)):
        result = result + s[j]*n
    print(result)
