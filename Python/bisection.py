def fDer(a, expr):
    if(a < -0.01 or a > 0.01):
        d = 0.01*abs(a)
    else:
        d = 0.0001
    x = a+d
    t1 = eval(expr)
    x = a-d
    t2 = eval(expr)
    t3 = 2*d
    f = (t1-t2)/t3
    return f


print("Please give termination parameter as zero to proceed with number of iterations.")
a, b, e = map(float, input(
    "Input lower limit,upper limit and termination parameter to find minimum in the interval (a,b): ").split())
expr = input("Enter expression for x: ")
print("Please give no. of iterations as considerably a high number to check with termination parameter.")
i = int(input("Enter number of iterations to be performed: "))
x = a
f1 = eval(expr)
x = b
f2 = eval(expr)
x1 = a
x2 = b
if(fDer(a, expr) < 0 and fDer(b, expr) > 0):
    print("Minimum exists in the given interval.")
else:
    print("Minimum doesn't exist.")
    exit(0)
c = 0
while(True):
    z = (x1+x2)/2
    print(x1, " ", z, " ", x2, " ")
    t = fDer(z, expr)
    if(abs(t) < e):
        break
    elif(t < 0):
        x1 = z
    else:
        x2 = z
    c += 1
    if(c >= i):
        break
print("Interval in which minimum lies is ({},{})".format(x1, x2))
z = (x1+x2)/2
print("Minimum of the function is at ", z)
