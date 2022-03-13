tc = int(input())
for i in range(0, tc):
    seq = list(map(int, input().split(' ')))
    hc = seq[0]
    m = 0
    for j in range(1, hc+1):
	m += seq[j]
    m = m/hc
    supc = 0
    for j in range(1, hc+1):
	print(seq[j], m)
	if seq[j] > m:
	    supc += 1
	else:
            pass
    print('%.3f'%(float(supc/hc*100)) + '%')
