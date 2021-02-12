def F(n):
    FibArray = [1, 1]
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


k = 2
a, b = map(float, input("Enter lower limit, higher limit: ").split())
choice = int(input(
    "Enter 0 to input number of iterations or enter 1 to input number of function evaluations: "))
if(choice == 0):
    n = int(input("Enter number of iterations: "))
    m = n+1
else:
    m = int(input("Enter number of function evaluations: "))
expr = input("Enter expression for x ")
L = abs(b-a)
k = 2
while(True):
    y = (F(m-k+1)/F(m+1))*L
    x1 = a+y
    x = x1
    f1 = eval(expr)
    x2 = b-y
    x = x2
    f2 = eval(expr)
    if(f1 < f2):
        b = x2
    else:
        a = x1
    if(k == m):
        break
    else:
        k = k+1
print("Minimum lies in the interval ", round(a, 5), " and ", round(b, 5))
