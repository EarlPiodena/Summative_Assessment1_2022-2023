import re

char_lower = '[a-z]'
char_higher = '[A-Z]'
num = '[0-9]'
char_spec = '[!, #, *]'
attempts = 5

print("Hello user! Please enter your password.")
print("It must contain at least:\n1. One lower case letter\n2. One upper case letter\n3. One of these special characters: !, #, *\n4. And minimum length of 6 and maximum length of 12 characters.")

while attempts > 0:
    password = input("Enter your password: ")
    
    if len(password) < 6 and len(password) > 12:
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif not re.search(char_lower, password):
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif not re.search(char_higher, password):
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif not re.search(num, password):
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif not re.search(char_spec, password):
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif re.search("\s", password):
        attempts -=1
        print(f"Incorrect password. No Whitespaces please. Attempts left: {attempts}")
        continue
    else:
        break

if attempts == 0:
    print("No more attempts! Please restart the program.")
else:
    print("Correct Password, Welcome User!")