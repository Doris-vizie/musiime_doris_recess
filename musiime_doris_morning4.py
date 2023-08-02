# Exercise 1; calculate and display area and circumference of a circle   
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def display_area(self):
        return 3.14 * (self.radius * self.radius)
    def display_circum(self):
        return 2 * 3.14 * self.radius
my_circle = Circle(2)
print("The area of the circle is: " + str(my_circle.display_area()))
print("The circum of the circle is: " + str(my_circle.display_circum()))

# Exercise 2; calculate employee's bonuses(15%) of salary employee salary(employee1 = 150000, employee2 = 230000)
class Employee:
    def __init__(self, salary):
        self.salary = salary
    def display_bonus(self):
        if self.salary > 200000:
            return (15/100) * self.salary
        else:
            return (10/100) * self.salary
employee1 = Employee(150000)
print(employee1.display_bonus())
employee2 = Employee(230000)
print(employee2.display_bonus())

# Convert temperature(37) Celsius to Fahrenheit temperature
class Temp:
    def __init__(self, temperature):
        self.__temperature = temperature
    def celsius_to_fahrenheit(self):
        return (self.__temperature * 9/5) + 32
my_temp = Temp(37)
print(f"{my_temp.celsius_to_fahrenheit()}°F")

# Assignment: Show encapsulation with employee information to give a pay increment (salary with employee information to  new_salary)
#e.g from 850000 to 1000000
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def display_salary_details(self):
        print(f"{self.__name} got an increment from {self.__salary} to {self.__salary + (self.__salary * 15/100)}")
my_employee = Employee("Doris", 850000)
print (my_employee.display_salary_details())
employee3 = Employee("Daren", 1000000)
print (employee3.display_salary_details())