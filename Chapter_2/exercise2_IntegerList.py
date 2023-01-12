#a variable that stores an empty list
num1 = []

#creates a for loop that stores 10 integers
for i in range(10):
    num = int(input("Enter a number: "))
    num1.append(num)

print(num1)

#output of the list using for loop
for i in num1:
    print(i)

#prints the highest and lowest number
print(max(num1))
print(min(num1))

#sorting the given elements in an ascending and descending order
num1.sort
print(num1)
num1.sort(reverse=True)
print(num1)

#appends 2 elements at the end of the list
num1.append(16)
num1.append(20)
print(num1)