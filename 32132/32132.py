input()
s = input()
while 'PS4' in s or 'PS5' in s:
    s = s.replace('PS4', 'PS').replace('PS5', 'PS')
    
print(s)
