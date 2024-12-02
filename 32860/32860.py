n, m = map(int, input().split())
if m <= 26:
    print(f'SN {n}{chr(64+m)}')
else:
    a = m // 26
    b = m % 26
    if b == 0:
        a -= 1
        b = 26
    print(f'SN {n}{chr(96+a)}{chr(96+b)}')
