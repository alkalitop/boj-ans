h, m = map(int, input().split(' '))
mp = m+15
hp = h+23+(mp//60)
print('%d %d'%(hp%24, mp%60))
