# 1. Create a Student class with name and age attributes. Print both values. 
# without object
class Student:
    name = "Rahul"
    age = 21
print(Student.name)
print(Student.age)

#  2. Create a Car class with brand and color attributes. 
# Create one object and display the details.
class car:
    brand = "BMW"
    color = "black"
c1 = car ()
print(c1.brand,
      c1.color)    

# 3. Create a Student class and create two objects: Rahul (21) and Priya (22).
class student:
    name = "rahul"
    age = 21
s1 = student() #obj 1
print(s1.name,
      s1.age)    

s2 = student () #obj 
s2.name = "priya"
s2.age = 22
print(s2.name,
      s2.age)

# 4. Create a Mobile class with brand and price. Display the details of two mobiles.
class mobile:
    brand = "Samsung S25"
    price = 150000
m1 = mobile ()
print(m1.brand,
      m1.price)
m2 = mobile()
m2.brand = "Realme"
m2.price = 20000
print(m2.brand,
      m2.price)
# here m1 ans n2 is object 

# 5. Create a Teacher class with name and subject. Print the teacher's details.
class teacher:
     T_Name = "Sapna"
     T_subject = "Data structure"
t1 = teacher ()
print (t1.T_Name,
       t1.T_subject)

# Create an Employee class with a constructor that accepts name and salary.
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        # self refers to the current object
        print(self.name)
        print(self.salary)

# Create an employee object
e1 = employee("Komal", 500000)

# Call the display method
e1.display()
 
# Create a Book class with title, author, and price using __init__().
class Book :
    def __init__(self, Tittle ,Author, Price):
        self.Tittle = Tittle
        self.Author = Author
        self.price = Price

    def display (self):
        print(self.Author)
        print(self.Tittle)
        print(self.price)


b1 = Book ("Good vives good life","vex king",500)
b2 = Book ("shutup","komal",0)

b1.display()
b2.display()

# Create a Laptop class with brand, RAM, and price. Create two objects with different values.
class laptop :
    def __init__(self ,brand ,ram ,price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def display (self):
        print(self.brand)
        print(self.ram)
        print(self.price)

l1 = laptop ("HP","8Gb",89000)
l2 = laptop ("macbook air ", "16gb", 10000)

l1.display()
l2.display()
       
# Create a BankAccount class with account_holder and balance. Display the account details.            # 

class BankAccount :
    account_holder = "Komal"
    balance = 119763890000000000000
print ("Name:",BankAccount.account_holder ,
       "balancee:",BankAccount.balance)    


# Create a Product class with product_name and quantity. Initialize the values using a constructor.
class product:
    def __init__(self,product_name , quantity):
        self.product_name = product_name
        self.quantity= quantity

    def display (self):
        print(self.product_name)
        print(self.quantity)

p1 = product ("cake", 4)
p2 = product ("pizaz",10)
p1.display()
p2.display()          



class movie:
    def __init__(self,name,cast):
        self.name = name 
        self.cast = cast
    def __str__(self):
        return f'Movie name is: {self.name} ans cast by: {self.cast}'
m1 = movie("ABCD","Varun Dhawan")
print(m1)      

class product:
    def __init__(self,items):
        self.items = items 
    def __len__(self):
        return len(self.items)
cart = product(["cpu","keybiad"])   
print(len(cart))  

 
# check code
# class Product:
#     def __init__(self, product_name, quantity):
#         self.product_name = product_name
#         self.quantity = quantity

# p1 = Product("Laptop", 5)

# print(p1.product_name)
# print(p1.quantity)

# 21 0ct 2026
# Q1. Instance Method Create a Student class with 
# an instance method display() that prints "Welcome to PIT".
class student:
    def display(self):
        print("welcome to the PIT")
s1 = student()        
s1.display()

# Q2. Instance Method with Object Data 
# Create an Employee class with a name variable. 
# Create two objects with different names and display 
# their names using an instance method.

class employee:
    def display(self):
        print("Instance Method with object ->",self.name)
e1 = employee()
e1.name ="komal" 
e1.display()      
e2=employee() 
e2.name='shiwani'
e2.display()

# Q3. Class Method Create a Student class with 
# a class variable school = "PIT". 
# Write a class method show_school() 
# to print the school name.

class student :
    school = "PIT"
    @classmethod
    def display(cls):
        print(cls.school)
student.display()        

 #  Q4. Class Method to Change Data Create a College class
 #  with a class variable name = "ABC College". 
 # Write a class method change_name() to change 
 # the college name to "PIT College".    

class college:
    cllg_name = "ABC college"
    @classmethod
    
    def change_name(cls,new_cllg_name): 
        cls.cllg_name=new_cllg_name

college.change_name("xyz")
print("updated cllg name ->", college.cllg_name)        

# Q5. Static Method Create a Calculator 
# class with a static method 
# multiply(a, b) that prints 
# the multiplication of two numbers.

class calcluator:
    @staticmethod
    def multiplication(a,b):
        print("static multiplication",a*b)
calcluator.multiplication(2,2)        

# Q6. Static Method Create a Number class 
# with a static method is_even(n) that 
# checks whether a number is even 

class number:

  @staticmethod
  def is_even(n):
    if n % 2 == 0:
      print("even")
    else:
      print("odd")
n1 = number()
# user_input = int(input("Enter a number: "))
# n1.is_even(user_input)

# Q7. Identify the Method Identify whether 
# the following is an instance method, 
# class method, or static method.
 


class Account:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    # 1. Official string representation
    def __repr__(self):
        return f"Account('{self.username}', {self.balance})"

    # 2. Truthiness: True if balance > 0, otherwise False
    def __bool__(self):
        return self.balance > 0

acc = Account("komal", 150)
print(repr(acc))  # Output: Account('Alice', 150)
print(bool(acc))  # Output: True (since balance > 0)

class Box:
    def __init__(self, volume):
        self.volume = volume

    def __lt__(self, other): return self.volume < other.volume   # <
    def __gt__(self, other): return self.volume > other.volume   # >
    def __le__(self, other): return self.volume <= other.volume  # <=
    def __ge__(self, other): return self.volume >= other.volume  # >=
    def __ne__(self, other): return self.volume != other.volume  # !=

b1 = Box(10)
b2 = Box(20)

print(b1 < b2)   # Output: True
print(b1 >= b2)  # Output: False
print(b1 != b2)  # Output: True

#  get item
class getitem:
    def __init__(self):
        self.drawers = {"top": "Socks", "bottom": "Shoes"}

    def __getitem__(self, drawer_name):
        return f"Found {self.drawers[drawer_name]} in the {drawer_name} drawer!"

# Testing
result = getitem()
# This triggers __getitem__
print(result["top"])     
print(result["bottom"])  

# set item()
class setitem:
    def __init__(self):
        self.content = {}

    def __setitem__(self, key, value):
        self.content[key] = value
        print(f"Stored {value} under the label '{key}'")

# Testing
box = setitem()
# This triggers __setitem__
box["toy"] = "Teddy Bear" 


# contains
class Box:
    def __init__(self):
        self.items = ["Gold", "Silver", "Diamonds"]

    def __contains__(self, item):
         return item in self.items

v1 = Box()
print("Gold" in v1)    
print("Copper" in v1)  


# call()
class AlarmClock:
    def __call__(self):
        print("BEEP! BEEP! Wake up!")

alarm = AlarmClock()
alarm() 



# iter and __next__
class Counter:
    def __init__(self, maximum):
        self.maximum = maximum
        self.current = 0

    def __iter__(self):
        self.current = 0 # Reset counter when loop starts
        return self      # Tells Python "I will handle the counting"

    def __next__(self):
        if self.current < self.maximum:
            self.current += 1
            return self.current
        else:
            raise StopIteration # Stops the loop cleanly when done

count_to_three = Counter(3)
for number in count_to_three:
    print(number)

# enter and exit 
class Room:
    def __enter__(self):
        print("💡Lights turned ON. Welcome!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(" Lights turned OFF. Goodbye!")
        return True # Tells Python everything closed safely

# Testing
# This triggers __enter__ at the start and __exit__ at the end
with Room():
    print("🚶 Walking around inside the room...")


#  opps questions 
# ENCAPSULATION 
# 1 Student Management System: Create a Student class 
# with attributes such as name, roll number, and marks. 
# Pass values using a constructor and 
# display student details using a display() method.

class student:
    def __init__(self,name ,roll_number , marks):
        self.name =name
        self.roll_number = roll_number
        self.marks = marks
    def display(self)  :
        print("NAME",self.name,
              "ROLL_NUMBER",self.roll_number,
              "MARKS",self.marks)
s1 = student("komal",9,90)
s1.display()

# 2. Bank Account System: Create a BankAccount class
#  with account holder name and balance. 
# Implement deposit() and withdraw() methods to manage transactions.

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money in the account!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. Remaining balance: ${self.balance}")


my_account = BankAccount("Komal", 100000.0)

my_account.deposit(500)   # Adds 500, balance becomes 1500
my_account.withdraw(200)  # Takes out 200, balance becomes 1300
my_account.withdraw(2000) # Prints: Not enough money in the account!


# 3. Employee Salary System: Create an Employee class 
# with name, employee ID, and basic salary.
#  Write a method to calculate the total salary by adding a 10% bonus.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(2000)

print(account.get_balance())


# 4. ATM PIN Security: Create an ATM class with a name-mangled __pin attribute.
#  Allow users to check their balance only after entering the correct PIN.

class ATM:
    def __init__(self, name, pin, balance):
        self.name = name
        self.__pin = pin 
        self.__balance = balance

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print(f"Welcome, {self.name}!")
            print(f"Your balance is: ₹{self.__balance}")
        else:
            print("Incorrect PIN! Access Denied.")


# Create an ATM object
atm = ATM("Komal", 1234, 5000)

# Enter PIN to check balance
pin = int(input("Enter your ATM PIN: "))
atm.check_balance(pin)


# 5. Student Marks Validation: Create a Student class with a __marks attribute. 
# Implement set_marks() to accept marks between 0 and 100 
# and get_marks() to display them.


class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully!")
        else:
            print("Invalid marks! Enter marks between 0 and 100.")

    def get_marks(self):
        print("Student marks:", self.__marks)


s1 = Student()

marks = int(input("Enter student marks (0-100): "))

s1.set_marks(marks)
s1.get_marks()

 


#  6 Online Shopping Wallet: Create a Wallet class with a __balance attribute. 
# Implement add_money() and make_payment() methods. 
# Prevent payments that exceed the available balance.

class wallet:
    def __init__(self,balance=0):
         self.__balance = balance
    def add_money(self,ammount):
        if ammount > 0 :
            self.__balance += ammount
            print("Money added")
        else :
            print("invaid ammount ")    
    def make_payment(self,ammount):
        if ammount <= 0 :
            print("invalid payment ammount")
        elif ammount > self.__balance:
            print("insuffucent Balance")
        else:
            self.__balance -= ammount
            print("payment done")    
    def show_balance (self ):
        print("Aval Balance : ₹", self.__balance)      
w = wallet()
amount = int(input("Enter amount to add: ₹"))
w.add_money(amount)

payment = int(input("Enter payment amount: ₹"))
w.make_payment(payment)
w.show_balance()

# INHERITANCE
#  7. 
# class Vehicle Management System: 
# Create a parent class Vehicle with a start() method. 
# Create child classes Car and Bike that inherit and use the parent method.

class vehicles:
     def start(self):
         print("Vehicle is Starting")
class car(vehicles):
     pass
class bike(vehicles):
     pass

c1=car()
b1=bike()
c1.start()
b1.start()

# 8. School Management System: 
# Create a parent class Person with name and age attributes. 
# Create child classes Teacher and Student 
# with additional attributes such as subject and course.

class Person: # person is the parent base class 
     def __init__(self, name, age): # __init__ is the constructor method that runs automatically when a new object is created.
         self.name = name
         self.age = age

class Teacher(Person): #teacher is the child class teacher inherits from person 

    def __init__(self, name, age, subject):
         super().__init__(name, age) #calls the parent Person class's constructor to set name and age, avoiding code duplication.
         self.subject = subject

    def display(self):
         print("Teacher Name:", self.name)
         print("Age:", self.age)
         print("Subject:", self.subject)

class Student(Person): #child class student , also inherit from the person 
     def __init__(self, name, age, course):
         super().__init__(name, age)
         self.course = course
     def display(self):
         print("Student Name:", self.name)
         print("Age:", self.age)
         print("Course:", self.course)

t1 = Teacher("Rahul", 30, "Python")
s1 = Student("Aman", 18, "B.Tech")
t1.display()
print()
s1.display()

# 9. Company Employee System: 
# Create a parent class Employee with name and salary attributes. 
# Create a child class Manager that inherits these attributes 
# and calculates salary with an additional bonus.

class Employee:
     def __init__(self, name, salary):
         self.name = name
         self.salary = salary

class Manager(Employee):
     def __init__(self, name, salary, bonus):
         super().__init__(name, salary)
         self.bonus = bonus
     def total_salary(self):
         return self.salary + self.bonus

m1 = Manager("Rahul", 50000, 10000)
print("Name:", m1.name)
print("Basic Salary:", m1.salary)
print("Bonus:", m1.bonus)
print("Total Salary:", m1.total_salary())

# Polymorphism

# 10. Animal Sound System: 
# Create three classes named Dog, Cat, and Cow. 
# Define a sound() method in each class that produces a different output.

class Dog: #They are completely independent of each other (there is no inheritance here).
     def sound(self):
         print("Dog says Woof!")

class Cat:
     def sound(self):
         print("Cat says Meow!")

class Cow:
     def sound(self):
         print("Cow says Moo!")

d = Dog()
c = Cat()
w = Cow()
d.sound()
c.sound()
w.sound()

  
# 11. Online Payment System: Create UPI, 
# CreditCard, and Cash classes.
#  Implement a pay(amount) method in each class that
#  displays a different payment confirmation message.

class UPI:
     def pay(self, amount):
         print("Paid ₹", amount, "using UPI")

class CreditCard:
     def pay(self, amount):
         print("Paid ₹", amount, "using Credit Card")

class Cash:
     def pay(self, amount):
         print("Paid ₹", amount, "using Cash")

p1 = UPI()
p2 = CreditCard()
p3 = Cash()
p1.pay(500)
p2.pay(1000)
p3.pay(200)

# 12. Shape Area Calculator: 
# Create Circle, Rectangle, and Square classes. 
# Define an area() method in each class to calculate 
# the area of the respective shape.

import math
class Circle:
     def __init__(self, radius):
         self.radius = radius
     def area(self):
         return math.pi * self.radius ** 2
class Rectangle:
     def __init__(self, length, width):
         self.length = length
         self.width = width
     def area(self):
         return self.length * self.width

class Square:
     def __init__(self, side):
         self.side = side
     def area(self):
         return self.side ** 2

c = Circle(5)
r = Rectangle(10, 5)
s = Square(4)

print("Circle Area:", round(c.area(), 2))
print("Rectangle Area:", r.area())
print("Square Area:", s.area())

# Abstraction
# 13. Online Payment Gateway: 
# Create an abstract class Payment with an abstract method pay(). 
# Implement this method in two child classes: UPIPayment and CardPayment.

from abc import ABC, abstractmethod #mports the necessary tools from Python's built-in Abstract Base Classes module.
class Payment(ABC): #class Payment(ABC) defines Payment as an abstract class
     @abstractmethod
     def pay(self):
         pass
class UPIPayment(Payment):#UPIPayment and CardPayment inherit from the abstract class Payment.
     def pay(self):
         print("Payment completed using UPI")
class CardPayment(Payment):
     def pay(self):
         print("Payment completed using Card")
p1 = UPIPayment()
p2 = CardPayment()
p1.pay()
p2.pay()

# 14. Transport Fare Calculator: 
# Create an abstract class Transport 
# with an abstract method calculate_fare(distance). 
# Implement the method in Bus, Taxi, and Auto classes using different fare rates.

class Transport(ABC):
     @abstractmethod
     def calculate_fare(self, distance):
         pass
class Bus(Transport):
     def calculate_fare(self, distance):
         return distance * 5
class Taxi(Transport):
     def calculate_fare(self, distance):
         return distance * 15
class Auto(Transport):
     def calculate_fare(self, distance):
         return distance * 10

b = Bus()
t = Taxi()
a = Auto()

print("Bus Fare: ₹", b.calculate_fare(10))
print("Taxi Fare: ₹", t.calculate_fare(10))
print("Auto Fare: ₹", a.calculate_fare(10))

# 15. Hospital Management System: 
# Create an abstract class HospitalStaff with an abstract method work().
#  Implement the method in Doctor, Nurse, and Receptionist classes 
# to display their respective responsibilities.

class HospitalStaff(ABC):
     @abstractmethod
     def work(self):
         pass
class Doctor(HospitalStaff):
     def work(self):
         print("Doctor treats patients")
class Nurse(HospitalStaff):
     def work(self):
         print("Nurse takes care of patients")
class Receptionist(HospitalStaff):
     def work(self):
         print("Receptionist manages appointments")

d = Doctor()
n = Nurse()
r = Receptionist()
d.work()
n.work()
r.work()

# Method Overriding
class father :
    def property(self):
        print("father has a house")
class son(father):
    def property (self):
        print("son has a car")
s1 = son ()
s1.property ()             

#  Q1. Create a Vehicle parent class with a start() method. 
# Create a Car child class and override the start() method.


class Vehicle:
    def start(self):
        print("Vehicle is starting...")
class car(Vehicle):
    def start(self):
        print("Car is starting with a roar")
c1 = car()
c1.start()  

# Q2. Create a Bank parent class with a display() method. 
# Create a SBI child class and use super() to call the parent method.

class Bank:
    def display(self):
        print("This is a general bank.")

class SBI(Bank):
    def display(self):
        super().display()
        print("This is an SBI bank.")

s1 = SBI()
s1.display()

# Q3. Create a Person class with a constructor accepting name. C
# reate a Student class with name and age.
#  Use super() to initialize the parent attribute.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age      
c1 = Student("Komal", 21)
print("Name:", c1.name)
print("Age:", c1.age)        

# Q4. Create an Employee parent class and a Manager child class. 
# Override the work() method and use super() to execute both methods.

class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        super().work()
        print("Manager is working with the team.")
c1 = Manager()
c1.work()        
