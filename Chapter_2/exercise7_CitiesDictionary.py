#making dictionary about three cities with three information, their country, their population, and their fact
cities = {"Tokyo City's Country" : "Japan",
          "Tokyo City's Population" : "13,960,000",
          "Tokyo City's Fact" : "There are vending machines in Tokyo that you can purchase almost anything from it, ranging from ramen, food, drinks, even clothes.",
          "Abu Dhabi City's Country" : "United Arab Emirates",
          "Abu Dhabi City's Population" : "1,540,000",
          "Abu Dhabi City's Fact" : "Abu Dhabi is one of the safest cities in the world.",
          "Iloilo City's Country" : "Philippines",
          "Iloilo City's Population" : "484,000",
          "Iloilo City's Fact" : "It is also known as the 'Heart of the Philippines"}

print("Information about these three cities, Tokyo, Abu Dhabi, and Iloilo:\n")
#printing the keys and values using for loop
for keys,values in cities.items():
    print(f"{keys} : {values}\n")