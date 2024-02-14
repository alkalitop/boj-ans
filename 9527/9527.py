c = [0]*55

for i in range(1, 55):
    c[i] = (c[i-1] << 1) + (1 << ~-i)

def calc (x):
    cnt = 0  
    b = bin(x)[2:]  
    z = len(b)
    for i in range(z):  
        if int(b[i]):
            v = z + ~i
            cnt += c[v]
            cnt -= (1 << v) + ~x
            x -= 1 << v
    return cnt  

a, b = map(int, input().split())
print(calc(b)-calc(a-1))
