while 1:
    n = int(input())
    s = []
    
    if n < 0: break
    
    for i in range(1, n):
        if n % i: continue
        s.append(i)
        
    if n == sum(s):
        print(f'{n} =', end=' ')
        print(*s, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')
        
