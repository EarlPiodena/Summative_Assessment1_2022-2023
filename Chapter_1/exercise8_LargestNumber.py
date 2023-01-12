#asks the user input of three numbers
num = int(input("Enter the first number: "))
num1 = int(input("Enter the second number: "))
num2 = int(input("Enter the third number: "))

#prints output of the greater number using ternary operator
print(num if num > num1 and num > num2 else num1 if num1 > num2 else num2, "is the greatest number")