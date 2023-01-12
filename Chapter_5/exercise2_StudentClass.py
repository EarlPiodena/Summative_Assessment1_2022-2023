class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        return round(avg, 1)

    def display(self):
        print(f'The average grade of student {self.name.title()} is {self.calcGrade()}')

name = input("Enter the student's name: ")
mark1 = int(input(f"Enter the English marks of {name.title()}: "))
mark2 = int(input(f"Enter the Math marks of {name.title()}: "))
mark3 = int(input(f"Enter the History marks of {name.title()}: "))

student1 = Student(name, mark1, mark2, mark3)
student1.display()