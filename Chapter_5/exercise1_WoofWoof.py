class Dog():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def display(self):
        print(f'\nThe Information about {self.name.title()} is:')
        print('Name:', self.name.title())
        print('Breed:', self.breed.title())
        print('Age:', self.age, 'years old')

    def oldest(self):
        print(f'\nThe oldest dog is {self.name.title()} with the age of {self.age}')

woof = Dog("batman", "doberman", "4")
woof.display()

woof2 = Dog("akira", "akita inu", "3")
woof2.display()

if woof.age > woof2.age:
    woof.oldest()
else:
    woof2.oldest()

