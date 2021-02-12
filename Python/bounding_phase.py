a, d = map(float, input("Enter initial point and delta: ").split())
expr = input("Enter expression for x: ")
x1 = a-d
x = x1
f1 = eval(expr)
x2 = a
x = x2
f2 = eval(expr)
x3 = a+d
x = x3
f3 = eval(expr)
if(f1 > f2 and f3 > f2):
    print("Minimum lies in the interval ({},{}).".format(x1, x3))
elif(f1 <= f2 and f1 <= f3):
    d = d*(-1)
i = 0
fn = f2  # function now
xn = x2  # x now
while(True):
    i += 1
    fp = fn  # function past
    xp = xn
    #print("x past", xp)
    xn = xp+pow(2, i-1)*d
    #print("x now ", xn)
    x = xn
    fn = eval(expr)  # function now
    if(fn >= fp):
        break
xpp = xp-pow(2, i-2)*d
if(d < 0):
    print("Minimum lies in the interval ({},{}).".format(
        round(xn, 5), round(xpp, 5)))
else:
    print("Minimum lies in the interval ({},{}).".format(
        round(xpp, 5), round(xn, 5)))
