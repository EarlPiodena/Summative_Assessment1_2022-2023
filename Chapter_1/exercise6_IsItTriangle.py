#def function to check the validity of the triangle
def triangle_validaity(num1, num2, num3):
    if num1 + num2 >= num3 and num2 + num3 >= num1 and num3 + num1 >= num2:
        return True
    else:
        return False

#creating a variable for the user input for three sides
tri_a = float(input("Enter length of side a: "))
tri_b = float(input("Enter length of side b: "))
tri_c = float(input("Enter length of side c: "))

#if else function to make a decision
out = triangle_validaity(tri_a, tri_b, tri_c)
if out == True:
    print("The triangle is valid\n")
    if tri_a == tri_b == tri_c:
        print("It is an Equilateral")
    elif tri_a == tri_b or tri_a == tri_c or tri_c == tri_b:
        print("It is an Isosceles")
    else:
        print("It is a Scalene")
else:
    print("The triangle is invalid")