def add(arth1, arth2):
    return arth1 + arth2

def sub(arth1, arth2):
    return arth1 - arth2

def mul(arth1, arth2):
    return arth1 * arth2

def div(arth1, arth2):
    return arth1 / arth2

def mod(arth1, arth2):
    return arth1 % arth2

arth1 = float(input("Enter the first number you want: "))
arth2 = float(input("Enter the second number you want: "))
res = int(input("Choose the arithmetic operation you want from: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\nEnter the number of your choice:  "))

if res == 1:
    result = add(arth1, arth2)
    print("The operation you have chosen is Addition, the result of the numbers you have given is: ", result)

elif res == 2:
    result = sub(arth1, arth2)
    print("The operation you have chosen is Subtraction, the result of the numbers you have given is: ", result)

elif res == 3:
    result = mul(arth1, arth2)
    print("The operation you have chosen is Multiplication, the result of the numbers you have given is: ", result)

elif res == 4:
    result = div(arth1, arth2)
    print("The operation you have chosen is Division, the result of the numbers you have given is: ", result)

elif res == 5:
    result = mod(arth1, arth2)
    print("The operation you have chosen is Modulus, the result of the numbers you have given is: ", result)

else:
    print("Invalid Input! Please restart the program and input a valid number.")
