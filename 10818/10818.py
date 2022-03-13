import sys
sys.stdin.readline()
seq = list(map(int, sys.stdin.readline().split(' ')))
print(min(seq), max(seq))
