import sys
T = int(sys.stdin.readline())

for i in range(0, T):
    N = int(sys.stdin.readline())
    card = sys.stdin.readline().split()
    s = [ card[0] ]
    for j in range(1, N):
        if ord(card[j]) <= ord(s[0]):
            s.insert(0, card[j])
        else:
            s.append(card[j])
    print(''.join(s))
