while 1:
    a, b = map(int, input().split())
    if not a: break
    print('neither' if a % b and b % a else ('factor' if a % b else 'multiple'))
