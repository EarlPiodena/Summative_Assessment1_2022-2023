a = 0
while True:
    a += 1
    c = input("Care to continue? Y/N: ")
    if c.upper() == 'N':
        break
    elif c.upper() == 'Y':
        continue
print(f"The user has executed the loop {a} times")
