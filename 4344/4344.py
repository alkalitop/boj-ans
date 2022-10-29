for i in range(int(input())):
    seq = list(map(int, input().split(' ')))
    m = sum(seq, -seq[0])/(len(seq)-1)
    cnt = 0
    for j in range(len(seq)):
        if j and seq[j] > m:
            cnt += 1
    p = (cnt/(len(seq)-1))*100
    print(f'{p:.3f}%')
