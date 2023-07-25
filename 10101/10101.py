a,b,c=map(int,[(i:=input)(),i(),i()]);print(a+b+c!=180 and'Error'or((a-b)*(b-c)*(c-a) and'Scalene'or(a==b==c and'Equilateral'or'Isosceles')))
