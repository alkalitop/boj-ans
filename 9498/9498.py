score = int(input())
st={'6':'D','7':'C','8':'B','9':'A','10':'A'}
print(st[str(int(score/10))] if score>=60 else 'F')
