import operator as op

print("Hello user! welcome to the calculator program.\nPlease choose a number from 1-6 to begin calculating:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Check greater number")


while True:
    
    userInput = input("Please choose what operation you would like to use to calculate:")
    
    if userInput.isdigit():
        
        if int(userInput) in range(1,7):
            
            str(userInput)
            break
        else:
            
            print("Invalid Input! Please enter a number from 1-6.")
            continue
    else:
        print("Incorrect input. Please try again.")
        continue


def add(list):
    sum = 0
    for x in list:
        sum = op.add(sum,x)
    return sum
def sub(list):
    diff = list[0] 

    n_indx = -(len(list) - 1) 

    for x in range(len(list) - 1):
        
        diff = op.sub(diff, list[n_indx])
        
        n_indx += 1

    return diff

def mul(list):
    prod = 1
    for x in list:
        prod = op.mul(x,prod)
    return prod
def div(list):
    quot = list[0]
    for x in list:
       
        quot = op.truediv(quot,x)
    return quot
def mod(list):
    
    remain = list[0]
    n_indx = -(len(list) - 1)
    for x in range(len(list) - 1):
        diff = op.mod(remain, list[n_indx])
        n_indx += 1
    return diff
def gt(list):
   
    lnumber = list[0]
    
    for number in list:
     
        if op.gt(number, lnumber):
            
            lnumber = number

    return lnumber


num = []


while True:
    
    usrInpt = input("Please enter a value or press q to quit and see the result: ")

    if usrInpt.isalnum(): 
        
        if usrInpt.isalpha():
            
            if usrInpt == "q" or usrInpt == "Q":
                break
            else:
                print("Invalid input. Try again.")
                continue
        else:
            num.append(int(usrInpt)) 
            continue
    else:
        print("Incorrect input. Please try again.")
        continue


userInput = int(userInput)

if userInput == 1:
    print("You have chosen to add the numbers and the result is:", add(num))

elif userInput == 2:
    print("You have chosen to subtract the numbers and the result is:", sub(num))

elif userInput == 3:
    print("You have chosen to multiply the numbers and the result is:", mul(num))

elif userInput == 4:
    print("You have chosen to divide the numbers and the result is:", div(num))

elif userInput == 5:
    print("You have chosen to find the modulo of the numbers and the result is:", mod(num))

elif userInput == 6:
    print(f"The greater number is: {gt(num)}")