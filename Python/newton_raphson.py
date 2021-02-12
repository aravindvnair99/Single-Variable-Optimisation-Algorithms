#8 Newton Raphson Method
from math import exp, sin, cos, log
#First derivative of a function
def fDer(a,expr):
  if(a<-0.01 or a>0.01):
    d=0.01*abs(a)
  else:
    d=0.0001
  x=a+d;t1=eval(expr)
  x=a-d;t2=eval(expr)
  t3=2*d
  f=(t1-t2)/t3
  return f
 
#Second derivative of a function
def fDDer(a,expr):
  if(a<-0.01 or a>0.01):
    d=0.01*abs(a)
  else:
    d=0.0001
  x=a+d;t1=eval(expr)
  x=a;t2=2*(eval(expr))
  x=a-d;t3=eval(expr)
  t4=d*d
  f=(t1-t2+t3)/t4
  return f
 
print("Please give termination parameter as zero to proceed with number of iterations.")
a,e=map(float,input("Input initial guess and termination parameter to find the minimum ").split())
expr=input("Enter expression for x: ")
print("Please give no. of iterations as considerably a high number to check with termination parameter.")
i=int(input("Enter number of iterations to be performed: "))
k=0
c=0
x=list()
x.append(a)
while(True):
  x.append(x[k]-(fDer(x[k],expr)/fDDer(x[k],expr)))
  c+=1
  if(c>=i or abs(fDer(x[k+1],expr))<e):
    break
  else:
    k+=1
print("Minimum of the function is at ",round(x[k+1],5))
