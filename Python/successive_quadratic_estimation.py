print("Please give termination parameter as zero to proceed with number of iterations.")
x = list()
x1, d, e = map(float, input(
    "Enter initial point, delta and termination parameter: ").split())
expr = input("Enter expression for x: ")
print("Please give no. of iterations as considerably a high number to check with termination parameter.")
j = int(input("Enter number of iterations to be performed: "))
x2 = x1+d
x = x1
f1 = eval(expr)
x = x2
f2 = eval(expr)
if(f1 >= f2):
    x3 = x1+2*d
else:
    x3 = x1-d
x = x3
f3 = eval(expr)
c = 0

while(True):
    Fmin = min(f1, f2, f3)
    if(Fmin == f1):
        xmin = x1
    elif(Fmin == f2):
        xmin = x2
    else:
        xmin = x3

    a0 = f1
    a1 = (f2-f1)/(x2-x1)
    a2 = (1/(x3-x2))*(((f3-f1)/(x3-x1))-a1)
    xbar = (x1+x2)/2-(a1/(2*a2))
    x = xbar
    fxbar = eval(expr)

    xlist = [x1, x2, x3, xbar]
    flist = [f1, f2, f3, fxbar]
    sortlist = sorted(flist)
    newx = list()
    newf = list()
    for i in range(3):
        # flist.index(sortlist[i]) returns index of corresponding f element in original list
        newx.append(xlist[flist.index(sortlist[i])])
    newx = sorted(newx)
    for i in range(3):
        # xlist.index(newx[i]) returns index of corresponding x element in original list
        newf.append(flist[xlist.index(newx[i])])
    x1, x2, x3 = newx
    f1, f2, f3 = newf
    #print("x values are",x1," ",x2," ",x3)
    newmin = xlist[flist.index(sortlist[0])]
    #print("new min is ",newmin)
    c += 1
    if((abs(Fmin-fxbar) < e and abs(xmin-xbar) < e)or c >= j):
        break
print("Point corresponding to x=", round(
    newmin, 5), " is the minimum of the function.")
