n = int(input("Enter any number that you wish to see in a multiplication table: "))
print(f"The multiplication table of {n} is: {n}")

a = 1
for i in range(10):
    print(f"{n} x {a} = {n * a}")
    for i in range(1):
        a+=1