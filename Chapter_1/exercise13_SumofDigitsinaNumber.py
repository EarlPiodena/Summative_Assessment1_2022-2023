def num_sum(n):
    brt = [int(i) for i in n]

    sm = 0

    for i in brt:
        sm+=i
    
    return sm, brt

pro_inp = input("Enter numbers: ")
sm, brt = num_sum(pro_inp)
print(f"{brt} = {sm}")