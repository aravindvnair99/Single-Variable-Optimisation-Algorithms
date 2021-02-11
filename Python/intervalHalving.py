# Algorithm for Interval Halving Method
# An alternative of eval function
from math import exp,sin,cos
def eval_expr(input_string):
     # Step 1
     allowed_names = {"sum":sum, "sin":sin, "cos":cos, "exp": exp, "pow":pow, "x":x}
     # Step 2
     code = compile(input_string, "<string>", "eval")
     # Step 3
     for name in code.co_names:
         if name not in allowed_names:
             # Step 4
             raise NameError(f"Use of {name} not allowed")
     return eval(code, {"__builtins__": {}}, allowed_names)

print("Please give termination parameter as zero to proceed with number of iterations.")
a,b,e=map(float,input("Enter lower limit, higher limit and termination parameter: ").split())
expr=input("Enter expression for x: ")
print("Please give no. of iterations as considerably a high number to check with termination parameter.")
i=int(input("Enter number of iterations to be performed: "))
c=0 # To maintain count of no. of iterations 
L=abs(b-a)
xm=(a+b)/2
while(True):  
    x=xm;fm=eval_expr(expr)
    x1=a+L/4
    x=x1;f1=eval_expr(expr)
    if(f1>fm):
        x2=b-L/4
        x=x2;f2=eval_expr(expr)
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
print("Minimum lies in the interval ",round(a,4)," and ",round(b,4))
