N = int(input())
for i in range(0, N):
    print(' '*(N-1-i)+'*'*(2*i+1))
for i in range(1, N):
    print(' '*i+'*'*(2*(N-1-i)+1))
