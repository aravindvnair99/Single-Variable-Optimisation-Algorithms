#Algorithm for Golden Section Search Method
import math
print("Pls give termination parameter as zero to proceed with number of iterations")
a,b,e=map(float,input("Enter lower limit, higher limit and termination parameter: ").split())
i=math.ceil(math.log(1/(b-a),0.618))
exprt=input("Enter expression for k: ")
if(e==0):
  print("(Pls give no. of iterations as considerably a high number to check with termination parameter)")
  i=int(input("Enter number of iterations to be performed: "))
c=0
xt="(w*({})+({}))".format(b-a,a)
expr=exprt.replace("k",xt)
print("New expr is ",expr)
a=0;b=1;L=1
while(True):
  w1=a+(0.618)*L
  w=w1;f1=eval(expr)
  w2=b-(0.618)*L
  w=w2;f2=eval(expr)
  if(f1<f2):
    a=w2
  else:
    b=w1
  L=abs(b-a)
  c+=1
  #print("a,b and L f1 and f2 are are",a," ",b," ",L," ",f1," ",f2)
  if(c>=i):
    break
#print("Minimum lies in the interval (without modifying)",a," and ",b)
w=a;a=eval(xt)
w=b;b=eval(xt)
print("Minimum lies in the interval ",round(a,4)," and ",round(b,4))
