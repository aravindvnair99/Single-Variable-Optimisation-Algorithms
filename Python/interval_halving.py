#3 Interval Halving Method
from math import exp, sin, cos, log
print("Pls give termination parameter as zero to proceed with number of iterations")
a,b,e=map(float,input("Enter lower limit, higher limit and termination parameter: ").split())
expr=input("Enter expression for x ")
print("(Pls give no. of iterations as considerably a high number to check with termination parameter)")
i=int(input("Enter number of iterations to be performed: "))
c=0
L=abs(b-a)
xm=(a+b)/2
while(True):  
    x=xm;fm=eval(expr)
    x1=a+L/4
    x=x1;f1=eval(expr)
    if(f1>fm):
        x2=b-L/4
        x=x2;f2=eval(expr)
        if(f2<fm):
            a=xm
            xm=x2
        else:
            a=x1
            b=x2
    else:
        b=xm
        xm=x1
    c=c+1
    L=abs(b-a)
    if(L<=e or c>=i):
      break
 
print("Minimum lies in the interval ",round(a,5)," and ",round(b,5))
