class Animal():

    def __init__(self, Type, Name, Colour, Age, Weight, Noise):
        self.type = Type
        self.name = Name
        self.colour = Colour
        self.age = Age
        self.weight = Weight
        self.noise = Noise
  
    def sayhello(self):
        print(f"\nHello! I am {self.name.title()}")

    def makeNoise(self):
        print(f"{self.noise.upper()}!")

    def animalDetails(self):
        print("\nDetailes about the animal:")
        print(f"Name: {self.name.title()}\nType: {self.type.title()}\nColour: {self.colour.title()}\nAge: {self.age}\nWeight: {self.weight}\nNoise: {self.noise.title()}")

cat = Animal("cat", "midnight", "black", 2, 4, "meow")
cat.sayhello()
cat.makeNoise()
cat.animalDetails()

lion = Animal("lion", "king", "gold", 8, 190, "rawr")
lion.sayhello()
lion.makeNoise()
lion.animalDetails()