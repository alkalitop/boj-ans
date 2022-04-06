seq = list(map(int, input().split()))

d = seq[1]-seq[0]
for i in range(2, 8):
    if (d != seq[i]-seq[i-1]):
        print('mixed')
        d = 0
        break
if d == 1:
    print('ascending')
elif d == -1:
    print('descending')
