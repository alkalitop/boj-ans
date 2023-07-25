t=0
while p:=print:
 try:a,b=input().replace('x','1j').split('=');t+=1;p('Equation #%d'%t);r=(v:=eval(a)-eval(b)).real;p((i:=v.imag)and'x = %.6f'%(-r/i)or(r and'No solution.'or'Infinitely many solutions.'));p()
 except:break
