from math import factorial
n, a, b, c = map(int, input().split())
print(factorial(n)//factorial(a)//factorial(b)//factorial(c))
