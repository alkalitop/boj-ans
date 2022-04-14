import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = sorted(list(map(int, input().split())))

def sol ():
    v = 0
    for i in range(n-2):
        a = card[i]
        if 3*a+2 > m:
            break
        for j in range(i+1, n-1):
            b = card[j]            
            if a+b*2+1 > m:
                break
            for k in range(j+1, n):
                c = card[k]
                num = a+b+c
                if num > m:
                    break
                elif num == m:
                    return m
                else:
                    if v == 0 or num > v:
                        v = num
    return v
        
print(sol())   
