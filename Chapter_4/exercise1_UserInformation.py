name = input("Enter your name: ")
age = input("Enter your age: ")
hometown = input("Enter your hometown: ")

filename = 'bio.txt'
with open('bio.txt', 'x') as file_handler:
    file_handler.write(f"Name: {name.title()}\n")
    file_handler.write(f"Age: {age}\n")
    file_handler.write(f"Hometown: {hometown.title()}")

print("\nYour Information:\n")
with open('bio.txt') as f:
    for line in f:
        print(line)