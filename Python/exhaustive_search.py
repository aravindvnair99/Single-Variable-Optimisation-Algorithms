a, b = map(float, input(
    "Input lower limit, upper limit to find minimum in the interval (a,b): ").split())
choice = int(input(
    "Input 0 to enter number of intervals or 1 to input number of decimal places for accuracy: "))
if(choice == 0):
    n = float(input("Input number of intervals: "))
else:
    t = float(input("Input number of decimal places for accuracy: "))
    n = 2*(b-a)*pow(10, t)
expr = input("Enter expression for x: ")
d = (b-a)/n
x1 = a
x = a
f1 = eval(expr)
x2 = x1+d
x = x2
f2 = eval(expr)
x3 = x2+d
x = x3
f3 = eval(expr)
while(True):
    if(f1 < f2 or f2 > f3):
        x1 = x2
        x = x1
        f1 = eval(expr)
        x2 = x3
        x = x2
        f2 = eval(expr)
        x3 = x2+d
        x = x3
        f3 = eval(expr)
    else:
        break
if(x3 <= b):
    print("Minimum lies in the interval ({},{})".format(
        round(x1, 5), round(x3, 5)))
else:
    print("No minimum exists in the given interval or the boundary point is the minimum point.")
