k = int(input())
a, b, c, d = map(int, input().split())
print(a*k+b == c*k+d and ('Yes ' + str(a*k+b)) or 'No')
