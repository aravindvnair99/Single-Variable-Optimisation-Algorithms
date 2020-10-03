#Algorithm for Fibonacci Search Method
import math
#Function to get Fibonacci numbers
def F(n):  
    FibArray = [1,1]       
    while len(FibArray) < n + 1:  
        FibArray.append(0)     
    if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = F(n - 1)  
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = F(n - 2)            
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]
k=2 #To keep a count of number of iterations
a,b=map(float,input("Enter lower limit, higher limit: ").split())
m=int(input("Enter number of function evaluations: "))
expr=input("Enter expression for x: ")
L=abs(b-a)
k=2
while(True):
  y=(F(m-k+1)/F(m+1))*L
  x1=a+y
  x=x1;f1=eval(expr)
  x2=b-y
  x=x2;f2=eval(expr)
  if(f1<f2):
    b=x2
  else:
    a=x1
  if(k==m):
    break
  else:
    k=k+1
print("Minimum lies in the interval ",a," and ",b)
