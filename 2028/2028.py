for _ in range(int(input())):
    n = input()
    print('YES' if str(int(n)**2)[-len(n):] == n else 'NO')    
