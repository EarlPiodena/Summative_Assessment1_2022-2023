petrol = []
price = []

with open("petrolPrice.txt") as file_handler:
    lines = file_handler.readlines()

for pevalue in lines:
    petrol.append(pevalue.split()[0])
for prvalue in lines:
    price.append(prvalue.split()[1])
    
petrol.remove("Liters")
price.remove("cost")

num = []
totpet = 0
totpri = 0

for x, y in zip(petrol, price):
    totpet = totpet + float(x)
    totpri = totpri + float(y)
    result = round(float(y) / float(x), 1)
    if result < 3.5:
        num.append(x)

avg = totpri / totpet

print("The average price per litre of petrol bought is:",round(avg, 1))

print("The petrol in litres that were bought at under 3.5 AED per liter are:")
for x in num:
    print(x)