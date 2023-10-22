n=int(input().split()[0]);print(*[([1]*5+[2]*7+[3]*12+[4]*17+[5]*20+[6]*17+[7]*12+[8]*7+[9]*5)[int(i)*100//n]for i in input().split()])
