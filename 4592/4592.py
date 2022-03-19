import sys
while 1:
    rl = sys.stdin.readline()
    if rl.strip() == '0':
        break
    seq = (rl.split())[1:]
    prev = ''
    filtered = []
    for i in range(0, len(seq)):
        if seq[i] != prev:
            filtered.append(seq[i])
            prev = seq[i]
    print(' '.join(filtered) + ' $')
