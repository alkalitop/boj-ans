import sys
input = sys.stdin.readline

n, m = map(int, input().split())
password = {}
for _ in range(n): 
    st, pw = input().split()
    password[st] = pw
for _ in range(m):
    print(password[input().rstrip()])
