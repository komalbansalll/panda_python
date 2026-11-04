# creatong class
class student: 
    def display(self):
        print("welcome")

# object 
s1 = student()       
s1.display()



# class with attributes and object
class student :
    name = "rahul"
    age = 21

#  creating obj to call class
s1 = student () #creates new object s1 is the variable that refers to that object.
print (s1.name)

s2 = student () #same class alwyas
s2.name = "priya"
s2.age = 22
print(s2.name)


# class is the Python keyword used to create a class.

# student is the class name.

# name = "rahul" is a class attribute.

# age = 21 is another class attribute.

# example
class car: #define a class name car
    brand='bmw' 
    color='purple'

car1=car()
print(car1.brand)
print(car1.color)

car2=car()
car.brand='tata'
car.color='black'
print(car2.brand)
print(car2.color)

car3=car()
car.brand="audi"
car.color="white"
print(car2.brand)
print(car2.color)

class fruit:
    a='apple'
    b='mango'

f1=fruit()
print(f1.a)
print(f1.b)

f2=fruit()
f2.a='cherry'
f2.b='banana'
print(f2.a)
print(f2.b)


#  __init__() constructor

class student:
    def __init__(self, name,age,city):
        self.name = name 
        self.age =age 
        self.city = city 
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("city:",self.city)

s1 = student("komal",22,"delhi")
s1.display()
  
# Instance Method works with the data of a particular object
class student:
    def display(self): #instance self refer to the current object
        print("hello")
s1 = student()   
s1.display()


class student:
    def display(self):
        print(self.name)
s1 = student()
s1.name = "komal"
s1.display() 

# Class Method works with class level dta uses @classmethod

class student:
    school  = "PIT" #difine class var

    @classmethod # coverts the method into class method
    def display(cls): #cls define class
        print(cls.school) # print class var school

student.display() 

# changing class level data

class student :
    school='pit'
    @classmethod
    
    def change_school(cls,new_school):
        cls.school=new_school

student.change_school('dps') 
print(student.school)

# decorator.  method

def my_decorator(func):
    def wrapper():
        print('before function')
        func()
        print('after function')
    return wrapper

@my_decorator
def hello():
    print('b')
hello()

# static method @staticmethod 
class cal :
    @staticmethod
    def add(a,b):
        print("staticmethod",a+b)

cal.add(10,10)

# pre-define method
# __init__method
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'student name : {self.name}'
    
       

s1=student('komal',24)   
print(s1.name,s1.age) 
print(s1)


# __del__method
class office:
    def __del__(self):
    
        print (f'object {self.name} is being finalized')

s1=office() 
s1.name='mansi'
del s1  
s2=office()  
s2.name='shiwani'
del s2   

# __len__method

class classroom:
    def __init__(self,students):
        self.students=students
    def __len__(self):
        return len(self.students)    
c1 = classroom(["komal","dev","shiwani"])
print(len(c1))
        

#  __add__()
class numbers:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value


n1 = numbers(1)
n2 = numbers(20)
print(n1+n2)

# __eq__()
class student:
    def __init__(self,marks):
        self.marks = marks
    def __eq__(self,other):
        return self.marks == other.marks
s1 = student(90)
s2 = student(90)    
s3 = student(75)
print(s1==s2)
print(s1==s3)

# __rep__()

class student:
    def __repr__(self):
        return "student object"
s = student()
print(repr(s))    


# __getitem__
class student :
    def __init__(self,name,marks ):
        self.name = name
        self.marks =marks
    def __getitem__(self, index):
        return self.marks[index]
s1 =student("komal",[10,20,90])    
print(s1[0])

# __bool__()

# __lt__() less then method
class student :
    def __init__ (self,age):
        self.age =age
    def __le__(self,other):
        return self.age <= other.age
    
s1 = student(4)
s2 = student(3)
print(s1<=s2)      


# __contains__ return true false
class student :
    def __init__(self,subjects):
        self.subjects =subjects
    def __contains__(self, subject):  
        return subject in self.subjects
s1 =    student (["python","ai","ds"])
print("python" in s1)


    # __call__()
class student :
    def __call__(self,name):
        print("hello",name)
s1 = student()
s1("kk")        

# __iter__()

# __next__()


# Encapsulation Binding data and methods together data protection

class student :
    def __init__(self,name,marks):
        self.name = name 
        self.__marks = marks
    def show(self):
        print("name",self.name)
        print("marks",self.__marks)
s1 = student("komal" ,90)
s1.show()




# inheritance
class parent :
    def show (self):
        print("this is parent class")
class child (parent):
    def display (self)     :

        print("this is child class")
obj = child() 
obj.show()
obj.display()      

# 1. The Parent Class (Base Class)
class Car:
    def drive(self):
        print("Driving on four wheels!")

# 2. The Child Class (Derived Class) - It inherits from Car
class ElectricCar(Car):
    def charge(self):
        print("Charging the battery...")

# --- Using the Classes ---

# Create a regular car
my_car = Car()
my_car.drive()      # Output: Driving on four wheels!

# Create an electric car
tesla = ElectricCar()
tesla.drive()       # Output: Driving on four wheels! (Inherited from Parent)
tesla.charge()      # Output: Charging the battery... (Child's own special feature)


# Inheritance  
# 1. What is Inheritance?
# Definition: Inheritance is an OOP concept in which one class 
# acquires the properties and methods of another class.
# In simple words, inheritance allows us to reuse the code of an existing 
# class without writing it again.
#   suppose we have parent calss - father and child class - son
# The son can use the properties and methods inherited from the father.

# Basic inheritance
class father :
    def house(self):
        print("father owns a house ")
class son (father):
    def car (self):
      print("sonowns a car")    
obj = son()
obj.house()
obj.car()          

# Single Inheritance
# When one child class inherits from only one parent class, it is called Single Inheritance.
class animal: # animal is parent class 
    def eat (self):
        print("eating  ")
class dog(animal): #dog is child class , Dog(Animal) establishes inheritance.
    def bark (self):
        print("dog barking")
obj = dog () 
obj.eat() 
obj.bark()              


# 2 Multiple Inheritance
# Definition: When one child class inherits from two or more parent classes, 
# it is called Multiple Inheritance.

class father :
    def skill1 (self):
        print("father : Driving")
class mother :
    def skill2 (self):
        print("mother : dancing")
class child(mother,father):
    def skill3(self):
        print("Child have 2 skills from mother and father")
obj = child()
obj.skill1()
obj.skill2()
obj.skill3()        

# 3 Multilevel Inheritance
# Definition: When a class inherits from another child class,
#  forming a chain of inheritance, it is called Multilevel Inheritance.


class grandfather : # Grandfather is the first parent class.

    def propertiy (self):
        print("grandfather : owns land")
class father (grandfather):
    def house (self):
        print("father : owns house")
class Child (father) :
    def car (self):
        print("Child owns BMW car")
        print("child indirectly inherits Grandfather's properties too.") # child indirectly inherits Grandfather's properties too.

obj = Child()
obj.propertiy()
obj.house()
obj.car()      

# 4. Hierarchical Inheritance
# Definition: When multiple child classes inherit from one common parent class,
#  it is called Hierarchical Inheritance.

class animal : #Animal is the common parent class.
     def sound (self):
        print("animals sound")
class dog (animal):
    def bark (self):
        print("dog bark")
class cat (animal):
    def meow (self):
        print("cat meow")  
class cow(animal):
    def moo (self):
        print("cow mooing🐮")
# Dog, Cat and Cow are child classes.

# a = animal()        
b = dog()
c = cat()
d = cow()
# a.sound()
b.bark()
b.sound()
c.meow()
d.moo()

#  5 Hybrid Inheritance
# Definition: When two or more types of inheritance are combined in a single program, 
# it is called Hybrid Inheritance.
                    
class person :
    def show_person(self):
        print("school person details")   
class student(person) :
    def study (self):
        print("student is studing")     
class teacher (person):#Student and Teacher inherit Person. (Hierarchical Inheritance)
     def teacher(self):
        print("Teachers is teaching")
class assistant (student,teacher):#Assistant inherits Student and Teacher. (Multiple Inheritance)
     def work (self):
        print("assistant is working ") 
obj = assistant()
obj.show_person()
obj.study()
obj.teacher()
obj.work()

# 3. Explanation
# Father is the Parent Class.
# property() is a method in the Father class.
# Son inherits the Father class.
# Son also defines property() with the same name.
# When we call s1.property(), Python executes the Son class method instead of the Father class method.
# Remember
# Method Overriding supports Runtime Polymorphism.


# Method Overriding
# Method Overriding means when a Child Class defines
#  a method with the same name as a method in the Parent Class, 
# the child class's method is executed when called on the child object.
class father :
    def property(self):
        print("father has a house")
class son(father):
    def property (self):
        print("son has a car")
s1 = son ()
s1.property ()  


# super()
class father :
    def show(self):
        print("father is a class")
class son(father):
    def show(self):
        super().show() #super() is used to call the parent class method.
        print("son is a class")
s1 = son ()
s1.show()        

# 3. Explanation
# class Father: – Parent class.
# class Son(Father): – Child class inherits Father.
# def show(self): – Son overrides the parent method.
# super().show() – Calls the parent's show() method.
# s1.show() – Executes the child method.

# Example – super() with Constructor
class person:
    def __init__(self,name):
        self.name =name
    def display (self):
        print("person name:",self.name)
class student(person):
    def __init__(self,name,age):
        super().__init__(name)    
        self.age = age
    def show(self):
        print("student name:",self.name)
        print("student age:",self.age)
s1 = student("komal",22)
s1.show()

# Explanation:
# Person is the Parent Class.
# Student is the Child Class.
# super().__init__(name) calls the Parent Class constructor.
# self.age = age initializes the child's own attribute.
# self.display() calls the inherited parent method to display the name.



