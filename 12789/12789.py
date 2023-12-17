n = int(input())

s1 = list(reversed(list(map(int, input().split()))))
s2 = []

t = 1

while 1:
    if len(s1)+len(s2) == 0:
        print('Nice')
        break
    if len(s1) and s1[-1] == t:
        s1.pop()
        t += 1
    elif len(s2) and s2[-1] == t:
        s2.pop()
        t += 1
    else:
        if (len(s1) and len(s2) and s1[-1] < s2[-1]) or (len(s1) and not len(s2)):
            s2.append(s1.pop())
        else:
            print('Sad')
            break
