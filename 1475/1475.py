S = input()
checker = [0]*10
for i in range(0, len(S)):
    k = int(S[i])
    if k == 6:
        if checker[6] <= checker[9]:
            checker[6] += 1
        else:
            checker[9] += 1
    elif k == 9:
        if checker[9] <= checker[6]:
            checker[9] += 1
        else:
            checker[6] += 1
    else:
        checker[k] += 1
print(max(checker))
