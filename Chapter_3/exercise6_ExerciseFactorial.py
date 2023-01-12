fa = 0
def fac(n):
    if n == 1:
        return 1
    else:
        fa = n * fac(n-1)
        return fa

a = int(input("Enter a number to find it's factorial: "))
print("The factorial of", a, "is", fac(a))