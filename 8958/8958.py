tc = int(input())
for i in range(0, tc):
    q = input()
    score = 0
    depth = 1
    for j in range(len(q)):
        if q[j] == 'O':
            score += depth
            depth += 1
        else:
            depth = 1
    print(score)
