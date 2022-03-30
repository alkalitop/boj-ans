input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = A - B
if not len(C):
    print(0)
else: 
    print(len(C))
    print(' '.join(map(str, sorted(list(C)))))
