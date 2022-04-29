n = int(input())

def sol(n):
    for i in range(n):
        if i+sum(list(map(int, list(str(i)))))== n:
            return i
    return 0
    
print(sol(n))  
