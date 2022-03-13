rest = []
for i in range(0, 10):
    rest.append(int(input()) % 42)
print(len(set(rest)))
