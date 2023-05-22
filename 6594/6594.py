t = 1

while 1:
    try:
        a, b = input().replace('x', '1j').split('=')
    except:
        break
    v = eval(a) - eval(b)
    if t > 1: print('')
    print(f'Equation #{t}')
    t += 1
    if v.imag == 0:
        if v.real == 0:
             print('Infinitely many solutions.')
        else:
            print('No solution.')
    else:
	    s = -v.real/v.imag
	    print('x = %.6f' % s)
