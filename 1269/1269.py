input()
A = set(input().split())
B = set(input().split())
print(len((A-B)|(B-A)))
