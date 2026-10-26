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
user_input = int(input("Enter a number: "))
n1.is_even(user_input)

# Q7. Identify the Method Identify whether 
# the following is an instance method, 
# class method, or static method.
 

 