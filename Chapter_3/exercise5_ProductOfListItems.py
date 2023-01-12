def pro(list):
    prod = 1
    for x in list:
        prod = prod * int(x)
    return prod

num = [1,11,16,16,19,64,70,3,2,97]
print("The product of the values inside the numList is", pro(num))