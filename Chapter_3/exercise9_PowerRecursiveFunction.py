def pow(base, power):
    if power == 0:
        return 1
    else:
        return base * pow(base, power - 1)

base = int(input("Enter a number for the base value: "))
power = int(input("Enter a number for the power value: "))
print(f"The value of {base} to the power of {power} is {pow(base,power)}")