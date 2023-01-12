class Employee:

    empCount = 0
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
        Employee.empCount += 1 

    def setData(self):
        return self.name, self.age, self.id, self.salary
    
    def getData(self):
        for x in emp_object:
            print(f"{x[0]}\t\t{x[1]}\t{x[2]}\t{x[3]}")

emp_object = [("Name", "Age", "ID", "Salary")]

for i in range(1,6):
    print("Details for employee number", i, ":")

    name = input("Enter employee's name: ")
    age = input("Enter employee's age: ")
    id = input("Enter employee's id: ")
    salary = input("Enter employee's salary: ")

    myEmployee = Employee(name.title(), age, id.upper(), salary)
    emp_object.append(myEmployee.setData())

print("\nEmployee data chart:")
myEmployee.getData()