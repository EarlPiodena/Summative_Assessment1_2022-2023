num = []

with open("numbers.txt") as file_handler:
    for lines in file_handler.readlines():
        num.append(lines.strip())

print("The numbers inside the list are:")
for x in num:
    print(int(x))