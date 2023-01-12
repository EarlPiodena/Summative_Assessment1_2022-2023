#creating a def function for adding two integers
def add(num1, num2):
    return num1 + num2

#asking the user to input two numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

#displaying the sum by calling the add function along with the user's inputs
print(f"The sum of {x} and {y} is {add(x,y)}")