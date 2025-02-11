n = int(input())
a = [' '*(n-i-1) + '*'*(2*i+1) for i in range(n)]
print('\n'.join(a[::-1][:-1] + a))
