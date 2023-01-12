#asks the users input of name, age and, place of birth
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
pob = input("Enter your place of birth: ")

#prints the output in a sentence
print("Hello", name.title() , ", you are", age , "years old by 2042", ", your place of birth is", pob.title())
print("The length of your name is: ", len(name) , "letters") #len is a function that takes the length of a given variable
print("You will be,", age+1 , "in 2023")

