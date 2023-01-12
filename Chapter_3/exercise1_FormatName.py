#asking user for their input
name = input("Please enter your first name: ")
name1 = input("Please enter your last name: ")

#using the f-string to display the given variables in a formatted text 
#using the title function to capitalize the first letters of the users name
print(f"Hello, {name.title()} {name1.title()}")