L, P = map(int, input().split())
A = map(lambda x: str(int(x)-L*P), input().split())
print(' '.join(list(A)))
