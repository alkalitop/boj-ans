a, b = map(int, input().split())

cnt = 1

while 1:
    if a == b:
        print(cnt)
        break

    if b > 0 and b % 2 == 0:
        b = b >> 1
        cnt += 1
    elif (b-1) % 10 == 0:
        b = (b-1)//10
        cnt += 1
    else:
        print(-1)
        break
