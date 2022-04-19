import sys
input = sys.stdin.readline

s = (1, 0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112, 1488801600)
for i in range(int(input())):
    print(s[int(input())])
    # OEIS A002898
