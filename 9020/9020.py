import sys
input = sys.stdin.readline

primes = [] # 10000 미만 소수
tmp = [1]*(10000)
cursor = 2
while cursor < 10000:
    if tmp[cursor]:
        rc = 10000 // cursor
        for i in range(1, rc):
            tmp[cursor*i] = 0
        primes.append(cursor)
    cursor += 1

T = int(input())

for i in range(T):
    g1, g2 = (0, 0)
    n = int(input())
    k = n//2
    while k > 1:
        if k%2 == 0 and k != 2:
            k -= 1
            continue       
        if k in primes and n-k in primes:
            g1, g2 = (k, n-k)
            break
        k -= 2
    print(g1, g2)
