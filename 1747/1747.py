n = int(input())

arr = [0]*(1003002)
for i in range(2, 1003002):
    if arr[i]: continue
    for j in range(1, 1003001//i+1):
        arr[i*j] = 1
    if str(i) == str(i)[::-1] and i >= n:
    	print(i)
    	break
