for i in range(int(input())):
    result = ''
    n, s = input().split()
    n = int(n)
    for j in range(len(s)):
        result = result + s[j]*n
    print(result)
